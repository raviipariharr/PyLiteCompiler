import subprocess
import os

def run_optimized_icg_phase(source_code):
    folder = 'Optimised_ICG'
    input_file = os.path.join(folder, 'inp.py')
    output_file = os.path.join(folder, 'output.txt')

    # Write user code to inp.py
    try:
        with open(input_file, 'w') as f:
            f.write(source_code)
    except Exception as e:
        return f"Failed to write input file: {e}"

    # Find executable
    exe_path = os.path.join(folder, 'a.exe')
    if not os.path.exists(exe_path):
        exe_path = os.path.join(folder, 'a.out')
        if not os.path.exists(exe_path):
            return "No executable (a.exe or a.out) found in Optimised_ICG."

    # Run compiler
    try:
        result = subprocess.run(
            [exe_path],
            cwd=folder,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        stderr_output = e.stderr.decode(errors='replace')
        stdout_output = e.stdout.decode(errors='replace')
        return f"Execution failed:\nSTDERR:\n{stderr_output}\nSTDOUT:\n{stdout_output}"

    # Read and return output
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading output file: {e}"
    else:
        return "output.txt not generated. Compiler might have failed or no valid input."

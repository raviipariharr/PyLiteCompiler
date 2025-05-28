import subprocess
import os

def run_ast_phase(source_code):
    folder = 'Abstract_Syntax_Tree'
    input_file = os.path.join(folder, 'inp.py')
    output_file = os.path.join(folder, 'output.txt')

    # Step 1: Write GUI input to the expected input file
    try:
        with open(input_file, 'w') as f:
            f.write(source_code)
    except Exception as e:
        return f"Error writing input file: {e}"

    # Step 2: Find and validate the executable
    exe_path = os.path.join(folder, 'a.exe')
    if not os.path.exists(exe_path):
        exe_path = os.path.join(folder, 'a.out')
        if not os.path.exists(exe_path):
            return "No executable (a.exe or a.out) found in Abstract_Syntax_Tree folder."

    # Step 3: Run the compiler executable
    try:
        subprocess.run([exe_path], cwd=folder, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return f"Compiler execution failed:\n{e.stderr.decode()}\n{e.stdout.decode()}"

    # Step 4: Read and return the output
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Failed to read output file: {e}"
    else:
        return "Output not generated. Compiler may have failed."

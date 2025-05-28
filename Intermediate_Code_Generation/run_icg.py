import subprocess
import os

def run_icg_phase(source_code):
    folder = 'Intermediate_Code_Generation'
    input_file = os.path.join(folder, 'inp.py')
    output_file = os.path.join(folder, 'output.txt')

    # Step 1: Save input code from GUI to input file
    try:
        with open(input_file, 'w') as f:
            f.write(source_code)
    except Exception as e:
        return f"Error writing to inp.py: {e}"

    # Step 2: Check for compiler executable
    exe_path = os.path.join(folder, 'a.exe')
    if not os.path.exists(exe_path):
        exe_path = os.path.join(folder, 'a.out')
        if not os.path.exists(exe_path):
            return "Executable (a.exe or a.out) not found in Intermediate_Code_Generation."

    # Step 3: Run the executable
    try:
        subprocess.run([exe_path], cwd=folder, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return f"Compiler failed:\nSTDERR:\n{e.stderr.decode()}\nSTDOUT:\n{e.stdout.decode()}"

    # Step 4: Read and return the output
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading output.txt: {e}"
    else:
        return "Output not generated. Compiler may have failed."

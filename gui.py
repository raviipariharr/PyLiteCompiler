import tkinter as tk
from tkinter import ttk, scrolledtext

from token_and_symbol_table.run_token import run_token_symbol_phase
from Abstract_Syntax_Tree.run_ast import run_ast_phase
from Intermediate_Code_Generation.run_icg import run_icg_phase
from Optimised_ICG.run_optimized_icg import run_optimized_icg_phase
from Target_Code.run_target_code import run_target_code_phase

root = tk.Tk()
root.title("PyLite Compiler")  # Title in the window bar
root.geometry("800x600")

# ----------------------
# Title Label on the GUI
# ----------------------
title_label = tk.Label(
    root,
    text="🧠 PyLite Compiler",
    font=("Helvetica", 24, "bold"),
    fg="#3B3B98"
)
title_label.pack(pady=10)

# Input label and text area
tk.Label(root, text="Input Code:").pack(anchor='w', padx=10, pady=(10,0))
code_input = scrolledtext.ScrolledText(root, height=10)
code_input.pack(fill='both', padx=10, pady=5, expand=True)

# Dropdown to select phase
tk.Label(root, text="Select Phase to Run:").pack(anchor='w', padx=10, pady=(10,0))
phase_selector = ttk.Combobox(root, values=[
    "Token and Symbol Table",
    "Abstract Syntax Tree",
    "Intermediate Code Generation",
    "Optimised ICG",
    "Target Code"
])
phase_selector.current(0)
phase_selector.pack(fill='x', padx=10, pady=5)

# Output label and text area
tk.Label(root, text="Output:").pack(anchor='w', padx=10, pady=(10,0))
output_box = scrolledtext.ScrolledText(root, height=10)
output_box.pack(fill='both', padx=10, pady=5, expand=True)

# Run button logic
def run_selected_phase():
    code = code_input.get("1.0", "end-1c")
    phase = phase_selector.get()

    try:
        if phase == "Token and Symbol Table":
            output = run_token_symbol_phase(code)
        elif phase == "Abstract Syntax Tree":
            output = run_ast_phase(code)
        elif phase == "Intermediate Code Generation":
            output = run_icg_phase(code)
        elif phase == "Optimised ICG":
            output = run_optimized_icg_phase(code)
        elif phase == "Target Code":
            output = run_target_code_phase(code)
        else:
            output = "Unknown phase selected."
    except Exception as e:
        output = f"Error while running phase:\n{str(e)}"

    output_box.delete("1.0", "end")
    output_box.insert("1.0", output)

# Run button
run_button = tk.Button(root, text="Run Selected Phase", command=run_selected_phase, bg="blue", fg="white")
run_button.pack(pady=10)

root.mainloop()

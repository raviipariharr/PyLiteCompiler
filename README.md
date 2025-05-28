# PyLiteCompiler

**PyLiteCompiler** is a lightweight compiler for a simplified version of the C programming language. It is designed to demonstrate the various phases of a compiler, from lexical analysis to code optimization, and includes a user-friendly GUI built with Python.

## 🚀 Features

- **Lexical Analysis**: Converts source code into tokens using Lex.
- **Syntax Analysis**: Builds an Abstract Syntax Tree (AST) using Yacc.
- **Semantic Analysis**: Performs type checking and builds a symbol table.
- **Intermediate Code Generation (ICG)**: Converts source into intermediate representations.
- **Code Optimization**: Enhances performance through optimized intermediate code.
- **Graphical User Interface**: Built with Tkinter for a clean and interactive experience.

## 🧾 Project Structure

```
PyLiteCompiler/
│
├── Abstract_Syntax_Tree/          # AST generation modules
├── Intermediate_Code_Generation/ # Intermediate Code Generator
├── Optimised_ICG/                 # Optimizer for intermediate code
├── token_and_symbol_table/       # Tokenizer and symbol table manager
├── gui.py                         # Main GUI file
└── README.md                      # Project documentation
```

## 🛠️ Installation

### Prerequisites

Make sure the following are installed:

- `flex` – Lexical analyzer generator
- `bison` – Parser generator
- `gcc` – C compiler
- `python3` – Python interpreter
- `tkinter` – Python GUI package (usually pre-installed)

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/raviipariharr/PyLiteCompiler.git
cd PyLiteCompiler

# On Ubuntu/Debian systems, install required packages
sudo apt update
sudo apt install flex bison gcc python3 python3-tk
```

## 📦 Usage

### Step 1: Compile Lexer and Parser

Navigate to the folder containing `lexer.l` and `parser.y` files, then run:

```bash
flex lexer.l
bison -d parser.y
gcc -o compiler lex.yy.c parser.tab.c -lfl
```

### Step 2: Run the GUI

In the root project directory, run:

```bash
python3 gui.py
```

The GUI will launch, allowing you to input, compile, and view analysis of your C-like code.

## 🎯 Learning Objectives

This project is ideal for:

- Understanding compiler architecture
- Exploring Lex and Yacc tools
- Visualizing intermediate code and optimization
- Building real-world compiler components in a simplified way






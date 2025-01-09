# COMPILER till Lexical Analysis

## Gamified Debugger

This project implements a gamified debugger for lexical analysis and syntax analysis in a compiler.

## Procedure to Run the Code

### Step 1: Install Requirements

#### Install Graphviz

Using Chocolatey (Windows):
```bash
choco install graphviz
```

Or download it from the official website: [Graphviz Download](https://graphviz.org/download/).

#### Install Python Dependencies

Run the following command to install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 2: Execute the Code

Run the main script with a sample C code file as input:
```bash
python src/main.py data/sample_c_codes/example1.c
```

# REFER THE BELOW INSTRUCTIONS 

1. ```bash```
   ```
   git clone https://github.com/gowdachaithanya-05/Compiler.git
   ```
2. Open two terminals (if in windows either powershell or wsl)
   > In the `first` terminal : 
   ```
   cd Compiler-Backend
   pip install -r requirements.txt
   uvicorn api_server.main:app --host 8000 
   ```

   > In the `second` terminal : 
   ```
   cd Compiler-Frontend
   npm i
   npm install
   npm run dev
   ```

   ### Happy ```Hacking``` !!! or should i say ```Compiling``` ;)

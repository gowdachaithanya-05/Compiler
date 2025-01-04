# api_server/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os
import base64
import json

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://localhost:8080",
    # Add any other origins you expect
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def parse_gcc_errors(stderr_output: str):
    """
    Parses GCC stderr output to extract error details.
    """
    errors = []
    for line in stderr_output.split('\n'):
        if line.strip() == "":
            continue
        # Example GCC error format:
        # path/to/file.c:line:column: error: message
        parts = line.split(':')
        if len(parts) < 4:
            continue
        try:
            file_path = parts[0]
            line_num = int(parts[1])
            column_num = int(parts[2])
            error_type = parts[3].strip().split(' ')[0]  # e.g., 'error'
            message = ':'.join(parts[3:]).strip()
            errors.append({
                "type": error_type.capitalize(),
                "message": message,
                "line": line_num,
                "column": column_num
            })
        except ValueError:
            continue
    return errors

def generate_ast_image():
    """
    Placeholder function to generate AST image.
    Replace with actual AST generation logic.
    """
    # For demonstration, returning None
    return None

@app.post("/compile")
async def compile_code(request: dict):
    try:
        code = request.get("code", "")
        if not code:
            raise ValueError("No code provided.")

        # Save the code to a temporary file
        os.makedirs("data", exist_ok=True)
        code_path = "data/user_code.c"
        with open(code_path, "w") as f:
            f.write(code)
        
        # Compile the code using gcc
        compile_process = subprocess.run(
            ["gcc", code_path, "-o", "data/user_program"],
            capture_output=True,
            text=True
        )

        if compile_process.returncode != 0:
            # Compilation failed, parse errors
            error_output = compile_process.stderr
            errors = parse_gcc_errors(error_output)
            return {
                "success": False,
                "errors": errors,
                "symbol_table": {},
                "ast_image": None
            }
        
        # If compilation is successful, proceed to lexical and syntax analysis
        # Placeholder for actual analysis
        symbol_table = {}  # Populate based on analysis
        ast_image = generate_ast_image()  # Generate AST image if applicable

        return {
            "success": True,
            "errors": [],
            "symbol_table": symbol_table,
            "ast_image": ast_image
        }
    
    except Exception as e:
        print(f"Error during compilation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

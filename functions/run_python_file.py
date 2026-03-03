import os
import subprocess
from functions.get_abs_path_in_wd import get_abs_path_in_wd
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description=
    """Runs a .py file as a subprocess, with the file being located in a 
    specified directory relative to the working directory. Returns a string 
    with the subprocess stdout, stderr and exit code""",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file to be ran, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Array of extra arguments to be passed on as parameters for the internal subprocess.run() call",
                items=types.Schema(type=types.Type.STRING),
            )
        },
        required=["file_path"]
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        target_dir = get_abs_path_in_wd(working_directory, file_path)
    except Exception:
        raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(target_dir):
        raise Exception(f'Error: "{file_path}" does not exist or is not a regular file')
    
    if file_path.split(".")[-1] != "py":
        raise Exception(f'Error: "{file_path}" is not a Python file')
    
    try:
        command = ["python", target_dir]
        if args:
            command.extend(args)

        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30)
        
        res_str = ""
    
        return_code = completed_process.returncode
        if return_code != 0:
            res_str += f'Process exited with code {return_code}'
        
        output = completed_process.stdout
        err = completed_process.stderr
        if not output and not err:
            res_str += "No output produced"
        else:
            res_str += f"STDOUT: {output}, STDERR: {err}"
            
        return res_str
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

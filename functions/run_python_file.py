import os
import subprocess
from functions.get_abs_path_in_wd import get_abs_path_in_wd

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

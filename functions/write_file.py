import os
from functions.get_abs_path_in_wd import get_abs_path_in_wd

def write_file(working_directory, file_path, content):
    target_dir = get_abs_path_in_wd(working_directory, file_path)
    
    if os.path.isdir(target_dir):
        raise Exception(f'Error: Cannot write to "{file_path}" as it is a directory')
        
    # Create necessary parent directories
    os.makedirs(os.path.dirname(target_dir), exist_ok=True)
    
    with open(target_dir, "w") as f:
        f.write(content)
        
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

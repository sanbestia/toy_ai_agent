import os

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    # Construct the full path to the target directory with the absolute working_directory and the directory argument
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
    # Check if target_dir falls within the absolute working_directory path
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        raise Exception(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if os.path.isdir(target_dir):
        raise Exception(f'Error: Cannot write to "{file_path}" as it is a directory')
        
    # Create necessary parent directories
    os.makedirs(os.path.dirname(target_dir), exist_ok=True)
    
    with open(target_dir, "w") as f:
        f.write(content)
        
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
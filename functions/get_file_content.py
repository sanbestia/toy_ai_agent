import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    # Construct the full path to the target directory with the absolute working_directory and the directory argument
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    if not os.path.isfile(target_dir):
        raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')
        
    # Check if target_dir falls within the absolute working_directory path
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        raise Exception(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    with open(target_dir, "r") as f:
        content = f.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
    return str(content)
    
    
def main():
    pass
    
if __name__ == "__main__":
    main()

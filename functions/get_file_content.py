import os
from functions.get_abs_path_in_wd import get_abs_path_in_wd
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    target_dir = get_abs_path_in_wd(working_directory, file_path)
    
    if not os.path.isfile(target_dir):
        raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')
    
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

import os
from functions.get_abs_path_in_wd import get_abs_path_in_wd
from google.genai import types
from config import MAX_CHARS


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads the contents of a file in a specified directory relative to the working directory, providing the first {MAX_CHARS} characters it contains.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file to be read, relative to the working directory",
            ),
        },
        required=["file_path"]
    ),
)



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

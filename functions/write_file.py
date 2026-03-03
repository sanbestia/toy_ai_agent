import os
from functions.get_abs_path_in_wd import get_abs_path_in_wd
from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Writes parameter-defined contents, passed as a string, into a file in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file to be written onto, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="String to be written onto the file present at [file_path]",
            )
        },
        required=["file_path", "content"]
    ),
)




def write_file(working_directory, file_path, content):
    target_dir = get_abs_path_in_wd(working_directory, file_path)
    
    if os.path.isdir(target_dir):
        raise Exception(f'Error: Cannot write to "{file_path}" as it is a directory')
        
    # Create necessary parent directories
    os.makedirs(os.path.dirname(target_dir), exist_ok=True)
    
    with open(target_dir, "w") as f:
        f.write(content)
        
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

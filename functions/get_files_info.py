import os
from functions.get_abs_path_in_wd import get_abs_path_in_wd
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)



def get_files_info(working_directory, directory="."): 
    target_dir = get_abs_path_in_wd(working_directory, directory)
    
    if not os.path.isdir(target_dir):
        raise Exception(f'Error: "{target_dir}" is not a directory')
    
    # Record contents of target directory onto a string to return
    target_dir_contents = []
    for item in os.listdir(target_dir):
        item_path = f'{target_dir}/{item}'
        target_dir_contents.append(
            f'- {item}: "file_size"={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}'
        )    
    contents_str = "\n".join(target_dir_contents)
    
    return contents_str
        
        
def main():
    print(get_files_info("."))

        
if __name__ == "__main__":
    main()

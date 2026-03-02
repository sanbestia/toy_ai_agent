import os

def get_files_info(working_directory, directory="."):
    try:     
        working_dir_abs = os.path.abspath(working_directory)
        # Construct the full path to the target directory with the absolute working_directory and the directory argument
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        if not os.path.isdir(target_dir):
            raise Exception(f'Error: "{target_dir}" is not a directory')
        
        # Check if target_dir falls within the absolute working_directory path
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        
        # Record contents of target directory onto a string to return
        target_dir_contents = []
        for item in os.listdir(target_dir):
            item_path = f'{target_dir}/{item}'
            target_dir_contents.append(
                f'- {item}: "file_size"={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}'
            )    
        contents_str = "\n".join(target_dir_contents)
        
        return contents_str
    
    
    except Exception as e:
        print(f'Error: {e}')
        
        
        
def main():
    print(get_files_info("."))

        
if __name__ == "__main__":
    main()

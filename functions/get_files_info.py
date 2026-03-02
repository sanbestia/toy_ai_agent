import os
from functions.get_abs_path_in_wd import get_abs_path_in_wd

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

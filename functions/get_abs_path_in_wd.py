import os

def get_abs_path_in_wd(working_directory, relative_path):
    
    working_dir_abs = os.path.abspath(working_directory)
    # Construct the full path to the target directory with the absolute working_directory and the directory argument
    target_dir = os.path.normpath(os.path.join(working_dir_abs, relative_path))
    
    # Check if target_dir falls within the absolute working_directory path
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        raise Exception(f'Error: Cannot access "{relative_path}" as it is outside the permitted working directory')
        
    return target_dir

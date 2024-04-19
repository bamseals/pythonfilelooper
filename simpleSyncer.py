import os
import shutil

def copy_files(source_dir, dest_dir):
    # Check if both paths are directories
    if not os.path.isdir(source_dir):
        print(f"Error: {source_dir} is not a valid directory.")
        return
    if not os.path.isdir(dest_dir):
        print(f"Error: {dest_dir} is not a valid directory.")
        return

    # Iterate through files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_file_path, source_dir)
            dest_file_path = os.path.join(dest_dir, relative_path)

            # Ensure the directory structure exists in the destination
            os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
            
            # Check if file already exists in the destination directory
            if os.path.exists(dest_file_path):
                # Check if the file sizes are different
                if os.path.getsize(source_file_path) != os.path.getsize(dest_file_path):
                    try:
                        # Copy the file to the destination directory
                        shutil.copy2(source_file_path, dest_file_path)
                        print(f"Copied {source_file_path} to {dest_file_path}")
                    except Exception as e:
                        print(f"Error copying {source_file_path} to {dest_file_path}: {e}")
            else:
                try:
                    # Copy the file to the destination directory
                    shutil.copy2(source_file_path, dest_file_path)
                    print(f"Copied {source_file_path} to {dest_file_path}")
                except Exception as e:
                    print(f"Error copying {source_file_path} to {dest_file_path}: {e}")

# Prompt user for folder paths
source_folder = input("Enter the path of the source folder: ")
destination_folder = input("Enter the path of the destination folder: ")

# Call the function to copy files
copy_files(source_folder, destination_folder)
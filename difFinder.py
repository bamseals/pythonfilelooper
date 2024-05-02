import os
from datetime import datetime

def write_unique_files_to_new_text(folder1, folder2):
    unique_to_folder1 = []
    unique_to_folder2 = []

    # Traverse folder1
    for root, dirs, files in os.walk(folder1):
        for file in files:
            source_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_file_path, folder1)
            dest_file_path = os.path.join(folder2, relative_path)

            # Check if the file exists in folder2
            if not os.path.exists(dest_file_path):
                unique_to_folder1.append(source_file_path)
            elif os.path.getsize(source_file_path) != os.path.getsize(dest_file_path):
                unique_to_folder1.append(source_file_path)

    # Traverse folder2
    for root, dirs, files in os.walk(folder2):
        for file in files:
            source_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_file_path, folder2)
            dest_file_path = os.path.join(folder1, relative_path)

            # Check if the file exists in folder1
            if not os.path.exists(dest_file_path):
                unique_to_folder2.append(source_file_path)
            elif os.path.getsize(source_file_path) != os.path.getsize(dest_file_path):
                unique_to_folder2.append(source_file_path)

    # Generate unique filename based on current date and time
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"unique_files_{timestamp}.txt"

    # Write results to the new text file
    with open(output_file, 'w') as f:
        f.write("Files unique to folder 1:\n")
        for file_path in unique_to_folder1:
            try:
                f.write(file_path + '\n')
            except:
                print("error writing " + file_path)
            f.write(file_path + '\n')

        f.write("\nFiles unique to folder 2:\n")
        for file_path in unique_to_folder2:
            try:
                f.write(file_path + '\n')
            except:
                print("error writing " + file_path)

    return output_file

# Prompt user for folder paths
folder1 = input("Enter the path of folder 1: ")
folder2 = input("Enter the path of folder 2: ")

# Write unique files to a new text file
output_file = write_unique_files_to_new_text(folder1, folder2)
print(f"Results written to {output_file}")
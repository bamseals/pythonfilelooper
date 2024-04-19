import os

def list_unique_files(folder1, folder2):
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

    return unique_to_folder1, unique_to_folder2

# Prompt user for folder paths
folder1 = input("Enter the path of folder 1: ")
folder2 = input("Enter the path of folder 2: ")

# Get lists of unique files
unique_to_folder1, unique_to_folder2 = list_unique_files(folder1, folder2)

# Print results
print("Files unique to folder 1:")
for file_path in unique_to_folder1:
    print(file_path)

print("\nFiles unique to folder 2:")
for file_path in unique_to_folder2:
    print(file_path)
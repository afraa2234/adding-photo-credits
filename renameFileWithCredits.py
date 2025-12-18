import os

# 🔹 Change this to the folder where your files are
folder_path = r"[FILE PATH HERE]"


# The text you want to append
append_text = " photo by [INSERT PHOTOGRAPHER NAME]"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Skip if it's a folder
    if not os.path.isfile(file_path):
        continue

    # Split name and extension
    name, ext = os.path.splitext(filename)

    # Create new filename
    new_name = f"{name}{append_text}{ext}"
    new_path = os.path.join(folder_path, new_name)

    # Rename the file
    os.rename(file_path, new_path)
    print(f"Renamed: {filename} -> {new_name}")

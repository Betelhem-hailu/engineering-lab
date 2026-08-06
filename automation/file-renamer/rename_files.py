from pathlib import Path


# 1. Find the folder containing our files
folder = Path("files")


# 2. Go through every file in the folder
for file in folder.iterdir():

    # 3. Ignore folders
    if not file.is_file():
        continue

    # 4. Get the file extension
    extension = file.suffix

    # 5. Create the new filename
    new_name = f"renamed_{file.stem}{extension}"

    # 6. Create the complete new path
    new_path = folder / new_name

    # 7. Rename the file
    file.rename(new_path)

    print(f"{file.name} → {new_name}")
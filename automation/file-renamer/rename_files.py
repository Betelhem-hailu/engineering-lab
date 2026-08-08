from pathlib import Path


# 1. Find the folder containing our files
folder = Path("files")

changes = []

# 2. Go through every file in the folder
for file in folder.iterdir():

    # 3. Ignore folders
    if not file.is_file():
        continue

    # 4. Get the file extension
    extension = file.suffix
    
    if extension == "":
        print(f"Skipping {file.name} as it has no extension.")
        continue
    if extension == ".mp4" or extension == ".mov":
        print(f"Skipping {file.name} as it is unsupported file.")
        continue

    # 5. Create the new filename
    new_name = f"renamed_{file.stem}{extension}"

    # 6. Create the complete new path
    new_path = folder / new_name

    changes.append((file, new_path))
    
print("\nChanges to be applied:") 
for file, new_path in changes: 
    print(f"{file.name} -> {new_path.name}")
        
print("Apply the changes? (y/n)")
ans = input().lower()
if ans != "y":
    print("Aborting...")
    exit()
    
renamed_count = 0 
for file, new_path in changes: 
    file.rename(new_path) 
    renamed_count += 1 
    
print("\nAutomation completed.") 
print("Summary:") 
print(f"Renamed: {renamed_count}") 
print(f"Skipped: {len(list(folder.iterdir())) - renamed_count}")

import shutil
import os

data_folder = "my_data"
os.makedirs(os.path.join(data_folder, "docs"), exist_ok=True)
with open(os.path.join(data_folder, "important.txt"), "w") as f:
    f.write("Important Data here")
with open(os.path.join(data_folder, "docs", "notes.md"), "w") as f:
    f.write("#Meeting Notes")
print(f"Created dummy folder for archiving: {data_folder}")

#... Create Zip archive
archive_name = "my_data_archive"

try:
    archive_path = shutil.make_archive(archive_name, 'zip', root_dir=data_folder)
    print(f"Archive created: {archive_path}")
    print(f"Does archive exist? {os.path.exists(archive_path)}")
except Exception as e:
    print(f"Error: {e}")
    
#Clear the files
if os.path.exists(data_folder):
    os.removedirs(data_folder)
print(f"Clened up data folder at {archive_path}.")
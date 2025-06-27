import shutil
import os

source_file = "source.txt"
with open(source_file, mode='w') as f:
    f.write("This is the original content")
print(f"Created Source file: {source_file}")

dest_file = "copied.txt"

try:
    shutil.copy(source_file, dest_file)
    print(f"Content of '{dest_file}': {open(dest_file).read()}")
except FileNotFoundError:
    print("Error: Source file not found")
except Exception as e:
    print(f"Error: {e}")

#Clear the files
if os.path.exists(source_file):
    os.remove(source_file)
if os.path.exists(dest_file):
    os.remove(dest_file)
print("Clened up dummy files.")
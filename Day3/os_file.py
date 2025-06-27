import os
file_path = "C:/python_day3/tmp/sam.txt"
path = "C:/python_day3/tmp/"

with open(file_path, mode='w') as f:
    f.write("Hellos")
os.makedirs(path, exist_ok=True)
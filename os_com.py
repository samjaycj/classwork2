import os

current_dir = os.getcwd()

print(f"Current working directory: {current_dir}")

new_dir = "./tmp"

if os.path.exists(new_dir) and os.path.isdir(new_dir):
    os.chdir(new_dir)
    os.mkdir(f"{os.getcwd()}/test")
    print(f"Changed Directory to : {os.getcwd()}")
else:
    print(f"Directory '{new_dir}' does not exist")
import os
import pathlib

# Current working Dir
print(pathlib.Path.cwd())
current_dir = pathlib.Path.cwd()

relative_file = pathlib.Path('important.txt')
print(f"Relative file path : {relative_file}")

absolute_path = pathlib.Path('/Python_day3/my_data/important.txt')
print(f"Absolute path: {absolute_path}")

joined_path = current_dir / 'my_data' / 'docs' / 'notes.md'
print(f"Joined Path : {joined_path}")

print(joined_path)
print(joined_path.name)
print(joined_path.parent)
print(joined_path.stem)
print(joined_path.suffix)
print(joined_path.anchor)
print(joined_path.parts)
print(absolute_path.name)
print(absolute_path.parent)
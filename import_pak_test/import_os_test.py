import os
import sys

curr_dir = os.getcwd()
print(f'Current dir: {curr_dir}')

prev_dir = os.path.join(curr_dir, '..', '')
print(f'Previous dir relative path {prev_dir}')

prev_abs_dir = os.path.abspath(prev_dir)
print(f'Previous dir absolute path {prev_abs_dir}')

prev_rel_dir = os.path.relpath(prev_abs_dir)
print(f'Previous dir relative path from current directory {prev_rel_dir}')

file_name = 'new.json'
print(f'Does file {file_name} exist: {os.path.exists(file_name)}')

file_name_abs_path = os.path.abspath(file_name)
print(file_name_abs_path)

print(sys.path)
sys.path.insert(0, prev_abs_dir)
print(sys.path)
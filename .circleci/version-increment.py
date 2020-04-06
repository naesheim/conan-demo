import fileinput
import os

version = os.environ.get('VERSION')
with fileinput.FileInput('conanfile.py', inplace=True,) as file:
    for line in file:
        if 'version' in line:
            line.yolo()
from os import system
import library

for i in library:
    system(f'pip install {i}')
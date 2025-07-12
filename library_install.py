from os import system
import library

def library_install():
    for i in library.library:
        system(f'pip install {i}')
from builtins import print

def library_add():
    next_library = list(input("Enter the next library : "))
    next_library_list = [next_library]

    with open('library.py', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if 'library = ["numpy", "pandas", "matplotlib",' in line:
            lines.insert(i + 1, 'library += next_library_list')
            break

    with open('library.py', 'w') as file:
        file.writelines(lines)

    print("library added successfully!")
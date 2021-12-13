def file(filename):
    try:
        with open(filename,"r"):
            print(filename.read())
    except FileNotFoundError :
        print(f"File {filename} is not found")

file('text_file.txt')

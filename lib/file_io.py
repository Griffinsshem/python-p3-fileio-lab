def write_file(file_name, file_content):
    full_path = f"{file_name}.txt"
    with open(full_path, mode="w") as full_path:
        full_path.write(file_content)

def append_file(file_name, append_content):
    full_path = f"{file_name}.txt"
    with open(full_path, mode="a") as full_path:
        full_path.write(append_content)

def read_file(file_name):
    full_path = f"{file_name}.txt"
    with open(full_path, mode="r") as full_path:
        return full_path.read()

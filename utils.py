
def read_all(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    return text 

def write_file(filepath, text):
    with open(filepath, 'w') as f:
        f.write(text)

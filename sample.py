

import semantic_kernel as sk

def read_all(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    return text 


filepath = "W:/Recordings/01/IS Fabric Bootcamp _ Session 7_ Fabric Data Warehouse and reporting (concepts and demo).vtt"

text = read_all(filepath)

print(text) 


print(sk.__version__)



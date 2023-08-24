

def read_all(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    return text 


filepath = "C:/DEV/Fabric Sessions/01/IS Fabric Bootcamp _ Kick off.vtt.cleaned.txt"

text = read_all(filepath)

print(text) 

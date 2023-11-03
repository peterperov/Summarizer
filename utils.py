import re
import docx

def read_all(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    return text 

def write_file(filepath, text):
    with open(filepath, 'w') as f:
        f.write(text)

def readtxt(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


def in_array(string, array):
    for regex in array:
        if re.search(regex, string):
            return True
    return False
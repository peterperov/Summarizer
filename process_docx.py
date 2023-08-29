# pip install python-docx

import docx
import re

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


filename = "C:/Meetings/05/IS Fabric Bootcamp _ Kick off.docx"

output = filename + ".complete.txt"

# print (readtxt(filename))

doc = docx.Document(filename)

regexArray = [  
    r'left the meeting',  
    r'joined the meeting',
] 


try: 
    streamWriter = open(output, 'w', encoding='utf-8')  

    for para in doc.paragraphs:
        if in_array(para.text, regexArray):
            # print("REGEX MATCH: " + para.text)
            continue

        # print(para.text)
        streamWriter.write(para.text + "\n")

finally: 
    streamWriter.close()


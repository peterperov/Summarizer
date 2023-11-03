# pip install python-docx

import docx
# import re

from utils import *


# filename = "C:/Meetings/09-Driving ADS with Azure Arc-enabled SQL Server_Feb 2023/Driving ADS with Azure Arc-enabled SQL Server_Feb 2023-en-US.docx"

def process_docx(filename):
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


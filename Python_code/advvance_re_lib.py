import re


#pattern=re.compile(r'\d{3}[.]\d{3}[-.]\d{4}')
#pattern=re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Za-z]\w*')
pattern=re.compile(r'[A-Za-z0-9]\w*@\w*\.(com|edu|net)')
#pattern=re.compile(r'[1-2]')
#pattern=re.compile(r'[^a-zA-Z0-9]')
#pattern=re.compile(r'[^b]at')
with open('data.txt','r') as read_file:
    file_reader=read_file.read()
    match=pattern.finditer(file_reader)
    for line in match:
        print(line)
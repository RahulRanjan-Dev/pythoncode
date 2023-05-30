import re

text_to_serach='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

ha  HaHa

Metacharcters (needs to be escaped)
. ^ $ * + {} [] \ | ()

coreyms.com
321-555-2677-1772
123.334.445.66776

Mr. Schafer
Mr Smith
Mrs. Robinson
Mr.T
'''

sent='''The sentence is 'He said "Hello there"'
The sentence is "He said 'Hello there'"'''
pattern=re.compile(r''''''(?:'|").*(?:'|")''')

match1=pattern.findall(sent)
print(match1)


sentence = 'Start a sentance and then bring it to end'

#pattern=re.compile(r'abc')
pattern=re.compile(r'end$')

matches=pattern.finditer(text_to_serach)

#  matches=pattern.findall(sentence)

for match in matches:
    print(match)

print(text_to_serach[1:4])
print()
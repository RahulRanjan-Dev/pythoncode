import re
import csv

CSV_SPLIT_RE = re.compile(r'''
(
[^,"]*?  #Either a series of non-double quote charcter
|        #or
"        #double quotes followed by
[^"]*(?:"[^,"]*"[^"]*)* # Match either a non-qiote,or 2 consequent double qotes inside double quotation mark
"        #Followed by closing double quote
)
(?:,|$)  #Followed by a commna or the end of string
''', re.VERBOSE)
with open(r"C:\Users\user\PycharmProjects\pythonProject\venv\test_data","r",encoding='utf-8') as file:
    read_csv=csv.reader(file)
    print(type(read_csv))
    with open("New_file.csv","w") as New_file:
        csv_writer=csv.writer(New_file,delimiter=',')
        for line in read_csv:
            quoted_values = CSV_SPLIT_RE.findall(line)
            print(line)
            print(line[0])
            print(line[1])
            print(line[3])
            csv_writer.writerow(line[0:3])



import csv
import os


#os.chdir()
dir="C:/Users/user/PycharmProjects/pythonProject/Data"
os.chdir(dir)
print(os.getcwd())
filename="annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
file=os.path.join(dir,filename)
print(file)

with open(file,newline='') as csv_f:
    csv_reader=csv.reader(csv_f,delimiter=',',)
    #next(csv_reader)
    with open("new_del_file.csv",'w') as new_file:
        csv_writer=csv.writer(new_file,delimiter='|')
        for line in csv_reader:
            csv_writer.writerow(line)


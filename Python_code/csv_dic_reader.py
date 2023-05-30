import csv
import os


#os.chdir()
dir="C:/Users/user/PycharmProjects/pythonProject/Data"
os.chdir(dir)
print(os.getcwd())
filename="annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
file=os.path.join(dir,filename)
print(file)

with open(file,'r') as csv_f:
    csv_reader=csv.DictReader(csv_f,delimiter=',')
    with open("new_dic_file.csv",'w') as new_file:
        Field_names=['Year','Industry_aggregation_NZSIOC','Industry_code_NZSIOC','Industry_name_NZSIOC','Units','Variable_code','Variable_name','Variable_category','Value','Industry_code_ANZSIC06']
        csv_writer=csv.DictWriter(new_file,fieldnames=Field_names,delimiter='|')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)


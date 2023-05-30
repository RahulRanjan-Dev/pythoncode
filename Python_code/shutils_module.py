import shutil
import gzip

shutil.make_archive('excrated_new_file','zip','excrated_file')
shutil.unpack_archive('archive_new.zip','unpacked_archive_new')
shutil.make_archive('excrated_new_file','gztar','excrated_file')

with open('data.txt','rb') as input_file:
    with gzip.GzipFile('daily_file.gz', 'wb') as output_file:
        shutil.copyfileobj(input_file,output_file)
        #fil.writelines(read_file)

with gzip.open('daily_file.gz','rb') as rf:
    c=rf.readlines()
    for line in c:
        print(line)



#shutil.copy('excrated_new_file','C:\Users\user\PycharmProjects\pythonProject\venv')
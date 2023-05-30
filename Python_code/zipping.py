import zipfile

# my_zip=zipfile.ZipFile("Archive_data.zip",'w')
# my_zip.write('data.txt')
# my_zip.close()

# with zipfile.ZipFile("archive_new.zip",'w') as file:
#     file.write('data.txt')

with zipfile.ZipFile('archive_new.zip','r') as f:
    f.extractall('excrated_file')
    # with open('excrated_file/data.txt','r') as read:
    #     read_con=read.readlines()
    #     for line in read_con:
    #         print(line)



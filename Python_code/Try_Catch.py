try:
    with open('data','r') as file:
        read_file=file.read()
        for line in read_file:
            print(line)
except Exception as e:
    print(e)
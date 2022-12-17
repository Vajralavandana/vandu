file = "C://Users//Vandana//Desktop//python.txt"
open_file = open(file, "r")
read_file = open_file.read()
print(read_file)


count = 1
while count<=3:
    file = "C://Users//Vandana//Desktop//python.txt"
    open_file = open(file, "r")
    read_file = open_file.read()
    print(read_file)
    count = count+1

with open(file, "r") as f:
    read_f = f.read()
    print(read_f)

count = 1
while count<=3:
    with open(file, "r") as f:
        read_f = f.read()
        print(read_f)
    count = count+1

with open("test.txt", "w") as f:
    f.write("Test the file writting using python")

count = 0
while count<=3:
    file_name = "test_"+str(count)+".txt"
    with open(file_name, "w") as f:
        f.write("Test the file writting using python")
    count = count+1

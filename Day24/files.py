'''my_file=open("myfile.txt")
contents=my_file.read()
print(contents)
my_file.close()'''

with open("myfile.txt") as f:
    contents=f.read()
    print(contents)


with open("myfile.txt", mode="a") as f:
    f.write("\nnew text")
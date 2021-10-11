#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
def getFileContents(file):
    list_contents=[]
    with open(file) as f:
        contents=f.readlines()
        #list_contents.append(contents)
        new_contents=[]
        for each in contents:
            str2 = each.replace("\n", "")
            new_contents.append(str2)

        return new_contents
file="C:\\career\\python_bootcamp\\100DaysPythonBootcamp\\Day24\\Mail+Merge+Project+Start (1)\\Mail Merge Project Start\\Input\\Names\\invited_names.txt"
contents=getFileContents(file)
print(contents)

with open(r"C:\career\python_bootcamp\100DaysPythonBootcamp\Day24\Mail+Merge+Project+Start (1)\Mail Merge Project Start\Input\Letters\starting_letter.txt") as f:
    main_contents=f.read()

with open("hello.txt", "a") as f:
    f.write(main_contents)



def writeToNewFile(contents):
    for each in contents :
        #print(main_contents)
        main_contents2=main_contents.replace("[name]", each)
        print(main_contents2)
        file=f"letter_for_{each}.txt"
        with open(file, mode="a") as f:
            f.write(main_contents2)
            #newfile_contents=f.read()
            #new_str=newfile_contents.replace("[name]", each)

writeToNewFile(contents)
print("\n\n------------------------------------||  Dictionary Of Words  ||-------------------------------------------")
f=open("file1.txt", "r")
if f.mode == 'r':
    contents =f.read().split()
    print("\n\n")
for i in contents:
    print("\t||",i,end=" || ")
while True:
    word = input("\n\n Choose a word ==>   ")
    if(word not in contents or word == ""):
        print("\n-----------------------------------||  Given Input is not present Choose Wisely !!! ||---------------------------------------\n ")
    else:
        print("\n----------------------------------||  You have following Alphabets  ||---------------------------------------\n\n")
        for i in word:
            print("\t||",i,end=" || ")   
        while True:
            counter1 = 0
            subst = input("\n\n\nChoose a substring from it ==>   ")
            for i in subst:
                if i not in word:
                    counter1 = 1
            if counter1 != 0:
                print("\n\t------------||  Choose Substring wisely !!!  ||------------------")
            else:
                while True:
                    print("\n\n-------------------------------||  Enter a string to check it is acceptable or not  ||----------------------------------------------- ")
                    string = input("\n\nString ==>  ")
                    counter = 0
                    for i in string:
                        if i not in word:
                            counter = 1
                    if counter != 0:
                        print("\n\t------------||  string is Not acceptable  ||------------------")
                    else:
                        if(subst in string):
                            print("\n\t------------||  string is acceptable  ||------------------")
                        else:
                            print("\n\t------------||  string is Not acceptable  ||------------------")
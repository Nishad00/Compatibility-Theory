while True:
    print("\n--------------------------------------------------------------------------------------------------------\n")
    print("\t\t\t | 1. | Equal no of a's followed by equal no of b's\n\t\t\t | 2. | First and last symbols are same\n\t\t\t | 3. | No of a's are divisible by 2\n\t\t\t | 4. | Binary no divisible by 5\n\t\t\t | 5. | No of a's divisible by 4 & No of b's are not divisible by 3 ")
    print("\n--------------------------------------------------------------------------------------------------------\n")

    choice = int(input("\nEnter your choice ==>  "))
    if(choice == 4):
        binaryno = int(input("\nEnter Binary no ==>  "))
        decvalue = 0
        base = 1
    else:
        string = input("\nEnter your String ==>  ")
        strlen = len(string)
    i = counter = counter2 = 0

    if(choice == 1):
    #     if(strlen%2==0):    
    #         while string[i] == "a":
    #             counter += 1
    #             if(i == strlen-1):
    #                 break
    #             else:
    #                 i = i+1

    #         while string[strlen-1] == "b":
    #             counter -= 1
    #             if(strlen == 0):
    #                 break
    #             else:
    #                 strlen -= 1

    #         if(counter == 0):
    #             print("\n:::: String is Acceptable")
    #         else:
    #             print("\n:::: String is Not Acceptable")
    #     else:
    #         print("\n:::: String is Not Acceptable")
    

        st=string
        counta=sum(map(lambda x : 1 if 'a' in x else 0, st))
        countb=sum(map(lambda x : 1 if 'b' in x else 0, st))
        if (counta == countb) and (counta > 0 ) and (len(st)==counta*2): 
            for i in st[0:(counta):1]: 
                if (i !='a'): 
                    print("String is wrong")
                    exit()
            print("string is right")
        else: print("String is wrong")
        

    if(choice == 2):

        if(string[0] == string[strlen-1]):
            print("\n:::: String is Acceptable")
        else:
            print("\n:::: String is Not Acceptable")
            
    if(choice == 3):
        for i in range(0,strlen-1):
            if(string[i] == "a"):
                counter += 1
            
        if(counter%2 == 0):
            print("\n:::: String is Acceptable")
        else:
            print("\n:::: String is Not Acceptable")

    if(choice == 4):
        temp = binaryno
        while(temp): 
            lastdigit = temp % 10 
            temp = int(temp / 10)          
            decvalue += lastdigit * base 
            base = base * 2 
        if(decvalue%5 == 0):
            print("\n:::: String is Acceptable")
        else:
            print("\n:::: String is Not Acceptable")



    if(choice == 5):
        for i in range(0,strlen ):
            if(string[i] == "a"):
                counter += 1
            if(string[i] == "b"):
                counter2 += 1
            
        if(counter%4 == 0 and counter2%3 != 0):
            print("\n:::: String is Acceptable")
        else:
            print("\n:::: String is Not Acceptable")
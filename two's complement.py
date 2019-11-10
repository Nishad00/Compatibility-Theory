while True:
    carry = 1
    flag = 0
    list1 = []
    list2 = []
    binary = input("\nEnter a Binary No ==>  ")
    for i in binary:
        if(i == "0"):
            list1.append("1")
        elif(i == "1"):
            list1.append("0")
        else:
            print("\n ------------------------------------ Entered no is not Binary --------------------------------------------- ")
            flag = 1
            break
    if(flag == 1):
        pass
    else:
        binary = ""
        binary = binary.join(list1)
        print("\n ###############   1's Complement is ==>    ",binary)
        list1.reverse()
        binary = ""
        binary = binary.join(list1)
        list1 = []
        for i in binary:
            if(i == "1" and carry == 1):
                list1.append("0")
            elif(i == "0" and carry == 1):
                list1.append("1")
                carry = 0
            else:
                list1.append(i)
        list1.reverse()
        binary = ""
        binary = binary.join(list1)
        print("\n ###############   2's Complement is ==>    ",binary)
        print("\n===================================================================================================================== ")


            


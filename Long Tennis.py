s = o = 0 
while True:   
    i = raw_input("\n----------------- enter who wins this match -------------------\n")
    if(i == 's' and s < 30):
        s += 15
    elif(i == 's' and s == 30 and s <= 40):
        s += 10
    elif(i == 's' and s >= 40):
        s += 1
        r = s - o
        if (r >= 2):
            print ("------------------- server win the game -------------------- ")
            exit()
    elif(i == 'o' and o < 30):
        o += 15
    elif(i == 'o' and o == 30 and o <= 40):
        o += 10
    elif(i == 'o' and o >= 40):
        o += 1
        r1 = o - s
        if (r1 >= 2):
            print ("------------------- opponent win the game -------------------- ") 
            exit()
    else:
        print("------------------------- Invalid Input ---------------------------------")
    if(s > 40 and o > 40 and s == o):
        s = o = 40
        print (s , o)
    else:
        print (s , o)  
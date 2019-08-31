amount = 0
print("\n-------------------- Welcome, Have a Drink ---------------------------\n")
print("\n*********** Only Coin of 25 & 100 Are Acceptable ************\n")
print("\n-----------------------------------------------------------------------\n")
while True:
    money = input("\n :::: Please Enter Money to buy cola =>  ")
    if(money == 25 or money == 100):
        amount += money
        if(amount >= 125): 
            amount -= 125
            print "\nHere have your cola and rest of your ",amount," Rs\n"
            exit()
    else:
        print "\nPlease only enter coin of 25 and 100 Rs other coins are not Acceptable\n"
        print "\n====== Here have your",money," Rs \n"
    

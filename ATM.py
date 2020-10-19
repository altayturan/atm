import os,time,sys

accountAltay={                          #This is my little user. I can add users only in scripts to 
                                        #system but i will 
    "Name":"ALTAY",                     #improve myself
    "Surname":"Turan",
    "AccountNumber":"1234",
    "password":"1234",
    "Balance":2000,
    "AdditionalBalance":1000
}

def AccountCheck():                #I'm checking Number and Password Here
    checkNumber=input("Enter Your Card Number: ")
    
    if (checkNumber==accountAltay["AccountNumber"]):
        
        checkPassword=input("\nEnter Your Password: ")
        
        if(checkPassword==accountAltay["password"]):
            print("\nLogin Succeed.\n\nYou Are Being Redirected.")
            time.sleep(2)
            os.system("cls")
            menu()
        else:
            print("\nWrong Password")
            input()
            os.system("cls")
            AccountCheck()
    else:
        print("\nWrong Number")
        input()
        os.system("cls")
        AccountCheck()
def menu():                        #My ATM's Menu
    print(f'''
    WELCOME {accountAltay["Name"]}
    
    1:  Balance Inquiry   
    2:  Pay  In
    3:  Withdraw
    4:  Exit
    ''')
    choose=input("Choose: ")
    
    if (choose=="1"):
        checkBalance()
    elif (choose=="2"):
        moneyIn()
    elif (choose=="3"):
        moneyOut()
    elif(choose=="4"):
        print("\n\nSee you!")
        time.sleep(2)
        sys.exit()
def moneyIn():                     #You can add money to your account here
    print("\nYou Are Being Redirected.")
        
    time.sleep(1)
    os.system("cls")
    print(f'''
    1-Balance: {accountAltay["Balance"]} Tl
    2-AdditionalBalance: {accountAltay["AdditionalBalance"]} Tl
    
    ''')
    choose=input("Where do you want to pay money in? : ")
    if (choose=="1"):
        newMoney=int(input("\nHow much do you want to pay in? : "))
        accountAltay["Balance"]+=newMoney
        time.sleep(2)
        print("\nSucceed")
        time.sleep(2)
        os.system("cls")
        menu()
    elif (choose=="2"):
        newMoney=int(input("\nHow much do you want to pay in? : "))
        accountAltay["AdditionalBalance"]+=newMoney
        time.sleep(2)
        print("\nSucceed")
        time.sleep(2)
        os.system("cls")
        menu()
def checkBalance():                #How much money do you have?
    print("\nYou Are Being Redirected.")
        
    time.sleep(1)
    os.system("cls")
        
    print(f'''
    Balance: {accountAltay["Balance"]} Tl
    AdditionalBalance: {accountAltay["AdditionalBalance"]} Tl
   
    ''')
        
    input("Press Enter To Return The Menu.")
    os.system("cls")
    menu()
def moneyOut():                    #You can lose all your money here be carefull
    print("\nYou Are Being Redirected.")
        
    time.sleep(1)
    os.system("cls")
        
    print(f'''
    1-Balance: {accountAltay["Balance"]} Tl
    2-AdditionalBalance: {accountAltay["AdditionalBalance"]} Tl
    ''')
    choose=input("Where do you want to withdraw money? : ")
    if (choose=="1"):
        newMoney=int(input("\nHow much do you want to withdraw? : "))
        accountAltay["Balance"]-=newMoney
        time.sleep(2)
        print("\nSucceed")
        time.sleep(2)
        os.system("cls")
        menu()
    elif (choose=="2"):
        newMoney=int(input("\nHow much do you want to withdraw? : "))
        accountAltay["AdditionalBalance"]-=newMoney
        time.sleep(2)
        print("\nSucceed")
        time.sleep(2)
        os.system("cls")
        menu()


AccountCheck()


#   SOME NOTES
#    
#   os.system("cls")= it's deleting all of the terminal.
#   time.sleep(second)=it's waiting and waiting for seconds
#
#
#
#set master password then aks for the users input
master_password = "password"
login= input("Enter Master-password: ")

#check if the password is correct
if login == master_password:
    
    #intro for the manage
    while login == master_password:
        print("""Options\n (1)List current accounts\n (2)Enter new account\n (3)Delete an account\n (4)Change Master-password\n (5)Exit""")
        options= int(input("\nPlease choose an option: "))
        
        if options == 1:
            #listing emails and current password
            password_list = open("pwdlst.txt", "r")
            password_list.seek(0)
            print("\n" + password_list.read())
            password_list.close()

        elif options == 2:
            #entering a new email and password
            account=input("\nEnter your account: ")
            username=input("\nEnter your account Username: ")
            email=input("\nEnter your email: ")
            passphase=input("\nEnter your passphrase: ")
            password_list = open("pwdlst.txt", "a")
            password_list.write(account + " - " + username + " - " + email + " - " + passphrase + "\n")
            password_list.close()

        elif options == 3:
            #deleting an account
            print("\nThis option is under construction")

        elif options == 4:
            #changing master password
            #try and use string formatting
            print("\nThis option is under construction")
            
        elif options == 5:
            #existing the app
            quit()

        else:
            print("Incorrect input! Please try again!")

else:
    print("Master-password was incorrect!")
    quit()
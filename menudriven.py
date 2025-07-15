print("select a number:")
print("\n 1. login \n 2. register \n 3. Dashboard \n 4. exit")


while True:
    
    a=int(input("Enter the Number: "))
    if(a==1):
        username=input("Enter the username: ")
        password=input("Entert the password: ")
        print(username , password)
    elif(a==2):
        Name=input("Enter the Name:")
        email=input("Enter the Mail: ")
        print("REgistration successfull")
    elif(a==3):
        print("Welcome to dashboard")
    elif(a==4):
        exit()
    else:
        pass

import random 
import string

passwords = {}

#load exiting password file
try:
    with open("passwords.text","r") as file:
        for line in file:
            website,password=line.strip().split(":")
            password[website]=password
except:
    pass

def generate_password():
    chars=string.ascii_letters + string.digits + "!@#$%^&"
    password="".join(random.choice(chars)for _ in range(8))  
    return password

while True:
    print("\n-----PERSONAL PASSWORD MANAGER-----") 
    print("1.Save password")         
    print("2.view Student")         
    print("3.Generate password")         
    print("4.Exit") 
    
    choice = input("enter your choice:")
    if choice == "1": 
        site = input("enter website:")
        password = input("enter password: ")       
        password[site] = password
        with open("password.text", "a") as file:
            file.write(f"{site}:{password}\n")
        
        print("Saved!")
        
    elif choice == "2":
        if not password:
            print("No data")
        else:
            for site,password in password.items():
                print(site, ":",password)  
    elif  choice == "3":
            print("Generated password", generate_password())
            
        
    elif choice =="4":
             print("ok bye..")
             break
    else:
             print("In-valid input")                
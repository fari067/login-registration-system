users=[]
logged_in_user=None
while True:
    print("\nLogin & Registration System")
    print("1.Register")
    print("2.Login")
    print("3.View Users")
    print("4.Logout")
    print("5.Change Password")
    print("6.Delete Account")
    print("7.Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        username=input("Enter username: ")
        password=input("Enter password: ")

        found=False
        for user in users:
            if user["username"].lower()==username.lower():
                found=True
                break
        if not found:
            newuser={
                    "username":username,
                    "password":password
            }
            users.append(newuser)
            print("Registration successful.")
                

        else:
            print("Username already exists.")

    elif choice=="2":
        username=input("Enter username: ")
        password=input("Enter password: ")
         
        found=False
         
        for user in users:
            if user["username"].lower()==username.lower() and user["password"]==password:
                found=True
                logged_in_user=user
                print(f"welcome,{username}!")
                break
        if not found:
            print("Invalid username or password.")

    elif choice=="3":
        if len(users)==0:
            print("No users found.")

        else:
            print("\n----User List----")
            for user in users:
                print("Username: ",user["username"])

    elif choice=="4":
        if logged_in_user:
            print(logged_in_user["username"],"Logged out successful.")
            logged_in_user=None

        else:
            print("No user is logged in.")

    elif choice=="5":
        if logged_in_user:
            old_password=input("Enter old password: ")

            if logged_in_user["password"]==old_password:
                new_password=input("Enter new password: ")
                logged_in_user["password"]=new_password

                print("Password changed successfully.")

            else:
                print("Wrong old password.")

        else:
            print("please login first.")

    elif choice=="6":
        if logged_in_user:
            users.remove(logged_in_user)
            print("Account deleted successfully.")
            logged_in_user=None

        else:
            print("please login first.")

    elif choice=="7":
        print("Exit")
        break

    else:
        print("Invalid choice.")

            

              
              

                  
                


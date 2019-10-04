while(True):
    name=input("Enter your User Name ; ")
    psw=input("Please Enter Your Password ;")

    
    if name=="admin" and psw=="admin":
        print("Well Come To HBL Account !!")
        break 
    else:
        print("Please Enter Your Correct User/Password !!")
        continue
    
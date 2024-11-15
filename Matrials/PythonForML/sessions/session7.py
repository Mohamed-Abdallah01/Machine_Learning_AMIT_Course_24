import random

def user_login():
    u = "admin"
    p = "1111"

    while True:
        x = input("Enter Your Name: ")

        if x == u:
            y = input("Enter The Password: ")

            if y == p:
                s = random.randrange(100, 10000000)  # Generate a random verification code
                print("Verification Code is:", s)

                while True:
                    i = int(input("Enter Verification code: "))

                    if i == s:
                        print(f"Welcome, {u}")
                        return
                    else:
                        print("Incorrect Verification Code, try again")
                break  # هذه السطر لن يتم الوصول إليه لأننا نعود من الدالة عند النجاح
            else:
                print("Incorrect password")
        else:
            print("Incorrect username")






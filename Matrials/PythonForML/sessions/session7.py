import random
from prettytable import PrettyTable

def user_login(username, password):
    u = "admin"
    p = "1111"

    while True:
        x = input("Enter Your Name: ")

        if x == username:
            y = input("Enter The Password: ")

            if y == password:
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

# استدعاء الدالة
user_login("admin", "1111")



products = [
    {"Name":"Salt" , "Price":1500 , "Quantity":12},
    {"Name":"chips" , "Price":2500 , "Quantity":150},
    {"Name":"cake" , "Price":800 , "Quantity":102},
    {"Name":"bread" , "Price":900 , "Quantity":79},
    {"Name":"water" , "Price":753 , "Quantity":159}
]

table = PrettyTable()
table.field_names = ['Name','Price','Quantity']

for prod in products:
    table.add_row([prod["Name"],prod["Price"],prod["Quantity"]])
print(table)


while True:
    product_name = input("Enter Product Name: ").lower()
    
    if product_name not in map(lambda x: x["Name"].lower() , products):
        print("Product not found in the table")
        continue
    
    quantity_required = float(input("Enter Quantity Required: "))
    
    product = next(p for p in products if p["Name".lower() == product_name])
    if quantity_required > product["Quantity"]:
        print("insufficient quantity . please enter new quantity ")
        continue
    
    discount_quantity = quantity_required // 250
    discount_percentage = 5.0 * discount_quantity
    total_discount = min(discount_percentage , 25.0)
    discount_price = quantity_required * product["Price"] *(1 - total_discount / 100)
    
    product["Quantity"] -= quantity_required
    
    total_discount_price += discounted_price
    print(f"Discounted Price: ${discount_price:.2f}")
    
    another_item = input("Do You Want Another Item? (yes or no ): ")
    if another_item.lower() != "yes":
        break

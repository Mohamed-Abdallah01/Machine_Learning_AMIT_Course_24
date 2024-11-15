import random
from prettytable import PrettyTable
from session7 import user_login
from second import total_discounted_price

user_login()

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

total_discounted_price(products)

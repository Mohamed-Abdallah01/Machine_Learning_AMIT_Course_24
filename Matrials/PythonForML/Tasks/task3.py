def functions1(username):
    print(F"Hello our new user{username}")
    
def SumNumbers(x,y):
    print(f"The First Number is {x} , The Second Number is {y} ")
    
functions1('mohamed')
SumNumbers(3,2)

def functions2(name,age=20):
    print(f"my name is {name} , and in the next july i wil be {age}")
    
functions2("mohamed")

def functions3(*data):
    names = list(data)
    new = input("Enter You First name:")
    names.extend(new.split())
    print(tuple(names))

functions3()

def functions4(**sum):
    print(sum)
    print(type(sum))
    
functions4(key1 = "moahmed" , key2 = 205.5)

functions_name = lambda x,y:x+y
print(functions_name(2,6))
print(type(functions_name))

def functions5(n):
    return lambda a:a*n

functions6 = functions5(2)
print(functions6(11))
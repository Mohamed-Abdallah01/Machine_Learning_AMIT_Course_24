#Calculator Task
"""
User Input:
The program should prompt the user to choose an operation from the following list:
- Addition
- Subtraction
- Multiplication
- Division
- Exit
Input Validation:
Ensure that the user inputs valid numbers for the calculations. If the input is invalid (e.g., non-numeric), prompt the user to enter the numbers again.
Performing Calculations:
Based on the user's choice, the program should ask for two numbers and perform the selected operation.
If the user selects division, check if the second number is zero to avoid division by zero errors.
Looping:
After each calculation, ask the user if they want to perform another calculation. If they answer "yes," return to the operation selection; if they answer "no," exit the program.
Output:
Display the result of the calculation in a user-friendly format.
For example: "The result of adding 5 and 3 is 8."
Exit Option:
If the user chooses to exit, print a thank you message and terminate the program.
Task Two:
Folder Operations with Files
In this
"""
user = input("Enter Your Name Please.")
print(f"Hello {user}")

print("Welcome To our Simple Calculator .")

FirstNmber = float(input("Enter The First Number :"))
SecondNumber = float(input("Enter The Second Number :"))

print("1.Summation")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

OperationNumber = input("Enter The Number Of Operation:")

if OperationNumber == '1':
    print(f"{FirstNmber} + {SecondNumber} = {FirstNmber+SecondNumber}")
elif OperationNumber == '2':
    print(f"{FirstNmber}-{SecondNumber} = {FirstNmber-SecondNumber}")
elif OperationNumber == '3':
    print(f"{FirstNmber} * {SecondNumber} = {FirstNmber*SecondNumber}")
elif OperationNumber == '4':
    print(f"{FirstNmber}+{SecondNumber} = {FirstNmber/SecondNumber}")
else:
     print("Please Enter The Number of operation.")




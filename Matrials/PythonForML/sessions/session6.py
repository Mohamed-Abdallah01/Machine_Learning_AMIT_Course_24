
# class fact_num:
#     def __init__(self , num):
#         self.num = num
#     def factorial(self):
#         if self.num == 0:
#             return 0
#         if self.num == 1:
#             return 1
#         return self.num * self.factorial(self.num -1)
# f1=fact_num(6)
# print(f1.factorial)

# class fact_num:
#     def __init__(self, num):
#         self.num = num

#     def factorial(self):
#         if self.num == 0:
#             return 0  # factorial of 0 should be 1
#         elif self.num == 1:
#             return 1
#         else:
#             return self.num * fact_num(self.num - 1).factorial()

# f1 = fact_num(6)
# print(f1.factorial())

def isPrime(num):
    for i in range(2 , num):
        if num % i == 0:
            return False
    return True

print(isPrime(5))
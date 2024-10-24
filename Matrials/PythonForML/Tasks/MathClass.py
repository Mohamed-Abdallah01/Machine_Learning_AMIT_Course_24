class Maths:
    def __init__(self, num1, num2=None):
        self.num1 = num1
        self.num2 = num2

    def is_prime(self):
        if self.num1 < 2:
            return False
        for i in range(2, self.num1):
            if self.num1 % i == 0:
                return False
        return True


    def common_divisors(self):
        if self.num2 is None:
            return []
        mn = min(self.num1, self.num2)
        common_list = []
        for i in range(1, mn + 1):
            if self.num1 % i == 0 and self.num2 % i == 0:
                common_list.append(i)
        return common_list





prime_check = Maths(16)
print(prime_check.is_prime())


common_div = Maths(6, 5)
print(common_div.common_divisors())

common_div_large = Maths(100, 80)
print(common_div_large.common_divisors())







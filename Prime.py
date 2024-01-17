class Prime:
    def primeFinder(n):
        for i in range(2, n):
            if n % i == 0:
                return False

        return True
#example number to check
number_to_check = 17
result = Prime.primeFinder(number_to_check)

if result:
    print(f"{number_to_check} is a prime number")
else:
    print(f"{number_to_check} is not a prime number")
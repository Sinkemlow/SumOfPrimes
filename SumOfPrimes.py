def is_prime(n):
    if n == 2:
        return True
    elif n % 2 != 0:
        for i in range(3, n):
            if n % i == 0:
                return False
        return True

prime_list = []
number = 2

while len(prime_list) < 1000:
    if is_prime(number):
        prime_list.append(number)
    number += 1

print sum(prime_list)


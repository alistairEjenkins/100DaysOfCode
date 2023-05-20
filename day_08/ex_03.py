# prime number checker

def is_prime(num):

    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for n in range(2, (num + 2) // 2):
            if num % n == 0:
                return False
        else:
            return True

for num in range(1,101):
    if is_prime(num):
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")

num = int(input("Which number do you want to check?\n>> "))
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
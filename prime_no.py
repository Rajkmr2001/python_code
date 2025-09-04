#7. Prime Checker Input a number and check if it is prime.
num = int(input("Enter a number :  "))
if num <= 1:
    print("not a  prime number")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"the number {num} is prime number")
else:
    print(f"the number {num} is not prime number")


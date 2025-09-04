 #5: Factorial Finder Input a number and print its factorial using a loop.
num = int(input("Enter the number:  "))
result = 1
n = num
while num > 1:
    result = result * num
    num = num - 1
print(f"the factorial of {n} is {result}")
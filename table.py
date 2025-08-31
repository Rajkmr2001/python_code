 #4: Multiplication Table Ask for a number and print its multiplication table (1 to 10).
num = int(input("Enter the Number:  "))
print(f"Table of {num} is: ")
for i in range(1,11):
        print(f"{i}x{num}={i*num}")
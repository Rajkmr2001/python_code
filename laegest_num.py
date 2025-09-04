#6. Max of Three Ask for three numbers and print the largest.
a = int(input("Enter the number 1:  "))
b = int(input("Enter the number 2:  "))
c = int(input("Enter the number 3:  "))
if a > b and a > c:
    print(f"the largest no. is :   {a}")
elif b >= a and b >= c:
    print(f"the largest no. is :   {b}")
else:
    print(f"the largest no. is :  {c}")

#10. Fibonacci Sequence
#Print the first n numbers of the Fibonacci series.
num = int(input("Enter the number of fibonacci series:  "))
a, b = 0, 1
print("Finbonacci series:   ")
for i in range(num):
    print(a, end=" ")
    a,b = b, a + b
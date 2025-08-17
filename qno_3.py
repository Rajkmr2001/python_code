#write a simple python program to store  seven fruits in a list entered by the user.
fruit = []
for i in range(7):
    l1 = input(f"enter fruit name {i+1}:  ")
    fruit.append(l1)
print("\nfruits list: " , fruit)
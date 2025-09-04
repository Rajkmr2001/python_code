8. #List Reversal Take a list from the user and print it reversed (without using reverse() method).
l1 = []
num = int(input("enter the Number element in list:  "))
for i in range(1, num +1):
    a = int(input(f"Enter the {i} element in list:  "))
    l1.append(a)
print(f"original list : {l1}")

#reverse list
reverse_list = []
for i in range(len(l1)-1, -1, -1):
    reverse_list.append(l1[i])
print(f"reverse list:  {reverse_list}")
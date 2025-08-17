#write a program to accept marks of 6 students and display them in a sorted manner
marks = []
for i in range(6):
    data = int(input(f"Enter the marks{i +1}:  "))
    marks.append(data)
marks.sort()
print(f"your sorted marks is: \n ", marks)
#9. Write a python program to check if a year is a leap year.
year = int(input("Enter year for search:  "))
if year % 4 == 0:
    print(f"{year } is leap year")
else:
    print(f"{year } is not a leap year")
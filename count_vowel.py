#9. Count Vowels
#Input a string and count the vowels in it.
a = input("Enter a word to count vowel: ").lower()  # make it lowercase
count = a.count("a") + a.count("e") + a.count("i") + a.count("o") + a.count("u")
print(f"Total vowels in '{a}': {count}")

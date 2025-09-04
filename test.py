a = input("Enter a word to count vowel: ").lower()
vowels = "aeiou"
count = 0

for char in a:
    if char in vowels:
        count += 1

print(f"Total vowels in '{a}': {count}")

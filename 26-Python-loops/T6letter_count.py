sentence = input("Enter a sentence: ")
letter_counts = {}

for char in sentence.lower():
    if char.isalpha():
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

for letter, count in sorted(letter_counts.items()):
    print(f"{letter}: {count}")
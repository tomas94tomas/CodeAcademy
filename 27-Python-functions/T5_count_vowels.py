def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

string1 = "Hello World"
string2 = "Python is fun"
string3 = "CodeAcademy"

print(f"'{string1}' has {count_vowels(string1)} vowels.")
print(f"'{string2}' has {count_vowels(string2)} vowels.")
print(f"'{string3}' has {count_vowels(string3)} vowels.")
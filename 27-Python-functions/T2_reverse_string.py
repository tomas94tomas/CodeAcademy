def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    test1 = "hello"
    test2 = "Python is fun"
    test3 = "12345"
    s = reverse_string

    print(f"Original: {test1} | Reversed: {s(test1)}")
    print(f"Original: {test2} | Reversed: {s(test2)}")
    print(f"Original: {test3} | Reversed: {s(test3)}")
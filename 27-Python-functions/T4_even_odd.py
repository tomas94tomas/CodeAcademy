def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

for i in range(1, 11):
    result = even_or_odd(i)
    print(f"{i} is {result}")

numbers = input("Enter numbers separated by spaces: ")
num_list = [int(num) for num in numbers.split()]
print("Largest:", max(num_list))
print("Smallest:", min(num_list))
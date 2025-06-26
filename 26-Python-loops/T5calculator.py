operator = input("Enter operation (+, -, *, /): ").strip()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        result = "Error: Cannot divide by zero!"
    else:
        result = num1 / num2
else:
    result = "Unknown operator."

print(f"Result: {result}")
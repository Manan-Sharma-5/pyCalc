print("Welcome to the Interactive Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")

choice = input("Enter choice: ")

if choice == "1":
    result = num1 + num2
    print("Result is:", result)
elif choice == "2":
    result = num1 - num2
    print("Result is:", result)
else:
    print("Invalid choice")

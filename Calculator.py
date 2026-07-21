num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

choice = input("Enter the operation: (Options +, -, *, /) ")

if choice == "+":
    Sum = num1 + num2
    print("Sum =", Sum)

elif choice == "-":
    Difference = num1 - num2
    print("Difference =", Difference)

elif choice == "*":
    Product = num1 * num2
    print("Product =", Product)

elif choice == "/":
    Division = num1 / num2
    print("Division =", Division)

else:
    print("No Valid input")

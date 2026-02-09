# Create a simple calculator program using python
# +,- ,*,/

try:
    # Simple Calculator

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter last number: "))

    if operator == "+":
        result = num1 + num2
        print("Result:", result)

    elif operator == "-":
        result = num1 - num2
        print("Result:", result)

    elif operator == "*":
        result = num1 * num2
        print("Result:", result)

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Syntax Error")

    else:
        print("Invalid operator")

except:
    print("Invalid operator")
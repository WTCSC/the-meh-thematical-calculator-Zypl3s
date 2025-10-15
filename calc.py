def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("your a moron")
        return None
    return a / b

def function():
    choice = input("wacha doin (add, subtract, multiply, divide): ")
    return choice

def again():
    agn = input("u trynna use ma calc again (yes/no): ").lower()
    if agn == "yes" or agn == "y":
        main()
    else:
        print("hasta la bye bye")
        exit()

def main():
    func = function()
    if func in ["add", "+", "subtract", "-", "multiply", "*", "divide", "/"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("your a moron")
            return

        if func == "add" or func == "+":
            print(f"The result is: {add(a, b)}")
        elif func == "subtract" or func == "-":
            print(f"The result is: {subtract(a, b)}")
        elif func == "multiply" or func == "*":
            print(f"The result is: {multiply(a, b)}")
        elif func == "divide" or func == "/":
            result = divide(a, b)
            if result is not None:
                print(f"The result is: {result}")
            else:
                print("no divide by zero idot")
    else:
        print("Invalid operation.")

    again()

main()
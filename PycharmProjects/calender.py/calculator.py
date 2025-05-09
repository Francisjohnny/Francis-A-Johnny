def add(n1, n2):
    return n1 + n2

"""TODO: Write out the other 3 mathematical functions. """
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    # Adding a check to avoid division by zero
    if n2 == 0:
        return "Division by zero is undefined!"
    return n1 / n2

# TODO: add these 4 functions into a dictionary as the values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# TODO: Use the dictionary operations to perform the calculations.
#  Multiply 4 * 17 using the dictionary.

# result = operations["*"](4, 17)
# Accessing the multiply function and passing 4 and 17
def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()

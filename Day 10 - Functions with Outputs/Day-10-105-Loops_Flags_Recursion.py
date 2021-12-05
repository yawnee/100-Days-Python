#Calculator

from art import logo


#Addition
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("what is the first number?: "))

    #prints the list of the keys in the dictionary
    for symbol in operations:
        print(symbol)

    Continue = True

    while Continue is True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what is the next number?: "))

        #Finds the operation in the dictionary
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. : ") == 'y':
            num1 = answer
        else:
            Continue = False
            calculator() #This allows you to refresh from the beginning for the user to keep going

calculator()

#Calculator

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

num1 = int(input("what is the first number?: "))

#prints the list of the keys in the dictionary
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("what is the second number?: "))

#Finds the operation in the dictionary
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)
1
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

#Why use return over print is that you can return the number and keep going, keep repluggin the return
operation_symbol = input("Pick an operation from the line above: ")
num3 = int(input("what is the next number?: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num3), num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

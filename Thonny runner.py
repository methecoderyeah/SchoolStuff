end_product = ""
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

while True:
    num1 = 1
    num2 = 1
    operation_dict = {
        "+": add(num1,num2),
        "-": subtract(num1,num2),
        "*": multiply(num1,num2),
        "/": divide(num1,num2),
    }


    def calculate():
        operation = input("+\n-\n*\n/\nWhat operation would you like to use?\n")
        num2 = float(input("What's the next number?\n"))
        su = operation_dict[operation]
        print(f"{num1} {operation} {num2} = {su}.\nThat is a basic mathematical fact!")
        num1 = su
        return num1, su


    num1 = float(input("What's the first number?\n"))
    operation = input("+\n-\n*\n/\nWhat operation would you like to use?\n")
    num2 = float(input("What's the next number?\n"))
    su = operation_dict[operation]
    print(f"{num1} {operation} {num2} = {su}.\nThat is a basic mathematical fact!")
    contin = True
    while contin == True:
        num1 = su
        con = input(f"type y to continue calculating with {end_product},\nor type n to use start a new calculation")
        if con == "y":
            calculate()
        else:
            contin = False
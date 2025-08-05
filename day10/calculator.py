def add (n1,n2):
    return n1 + n2

def sub (n1,n2):
    return n1 - n2

def mul (n1,n2):
    return n1 * n2

def divde (n1,n2):
    return n1/n2


# storing functions in dictiionary
operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : divde
}
def calculator():
    should_accumulate = True

    num1 = float(input("what is your first number ? "))

    while should_accumulate:  
        for symbols in operations:
            print(symbols)

        operation_symbol = input("pick one operation to perform ")
        num2 = float(input("what is your second number ? "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"type 'y' to continue calulations with {answer} or type 'n' for new operations ")

        if choice == 'y':
            num1= answer
        else:
            should_accumulate:False
            print("\n "* 20)
            calculator()
            # using recursion calling a function inside itself



calculator()
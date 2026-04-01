# python basic projects:
history = []

def calculate(num1,num2,operator):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return num1/num2
    else:
        return None
    
def print_history():
    print("\n------history------")
    for h in history:
        print("=>", h)
    print("---------------------\n")

while True:
    n1 = input("Enter 1st number:")
    if n1 == "exit":
        break
    elif n1 == "history":
        print_history()
        continue

    n2 = input("Enter 2nd number:")
    if n2 == "exit":
        break
    elif n2 == "history":
        print_history()
        continue

    operator = input("Enter operation(+,-,*,/):")
    if operator == "exit":
        break
    elif operator == "history":
        print_history()
        continue

    result = calculate(int(n1),int(n2),operator)
    if result:
        r = f"{n1}{operator}{n2} = {result}"
        # store the history
        history.append(r)
        print(r)
    else:
        print("Invalid input, please Try again")
    


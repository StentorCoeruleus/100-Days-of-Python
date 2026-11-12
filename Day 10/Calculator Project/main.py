import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
game_running=True
same_calculation=False
saved_answer=""

while game_running:

    if not same_calculation:
        first_number=float(input("Enter your first number:\n"))
        for key in operations:
            print(key)
        operator = input("Enter your operator:\n")
        second_number = float(input("Enter your second number:\n"))
        answer = operations[operator](first_number, second_number)

        print(f"{first_number} {operator} {second_number} = {answer}")

        continue_calculation = input(f"Type 'ans' to continue calculating with {answer}, or type 'no' to start a new calculation, or type 'exit' to quit.\n ").lower()

        if continue_calculation == "no":
            print("\n" * 100)
            same_calculation = False

        elif continue_calculation == "ans":
            saved_answer = answer
            same_calculation = True

        elif continue_calculation=="exit":
            game_running = False
        else:
            print("Sorry, that wasn't an option. Starting a new calculation...")

    elif same_calculation:
        first_number=float(saved_answer)
        for key in operations:
            print(key)
        operator=input("Enter your operator:\n")
        second_number=float(input("Enter your second number:\n"))
        answer=operations[operator](first_number,second_number)

        print(f"{first_number} {operator} {second_number} = {answer}")

        continue_calculation=input(f"Type 'ans' to continue calculating with {answer}, or type 'no' to start a new calculation, or type 'exit' to quit.\n ").lower()

        if continue_calculation=="no":
            print( "\n" *100)
            same_calculation=False

        elif continue_calculation=="ans":
            saved_answer=answer

        elif continue_calculation=="exit":
            game_running=False
        else:
            print("Sorry, that wasn't an option. Continuing with your last answer...")
            saved_answer=answer















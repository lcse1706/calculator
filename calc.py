import os

def welcome():
    print("Welcome to the Calculator !")
    print("It supports addition, subtraction, multiplication and division.")
    print("To exit, type 'exit'.\n")

def print_result(result):
    print("Result:", result)
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number(prompt):
        while True:
            num_str = input(prompt)
            if num_str == "exit":
                return num_str
            if num_str.isdigit() or (num_str.startswith("-") and num_str[1:].isdigit()):
                return float(num_str)
            print("Invalid input. Please enter a number.")

    
def check_numbers1(x):
    return int(x)
    
def get_operator():
    while True:
        operator = input("Enter operator (+,-,*,/): ")
        if operator in ["+", "-", "*", "/"]:
            return operator                                   
        if operator == 'exit':
            return operator
        print("Invalid input. Please enter (+,-,*,/).")

def calulate(x,y,operator):
    while True:
        if operator == "+":
            return x+y
        elif operator == "-":
            return x-y
        elif operator == "*":
            return x*y
        elif operator == "/":
            return x/y
            
def run_calculator():
    
    x = get_number('Please enter first numer: ')
    if x == 'exit':
        return False
    y = get_number('Please enter second number: ')
    if y == 'exit':
        return False
    operator = get_operator();
    if operator == 'exit':
        return False
    
    result = calulate(x, y, operator)
    print_result(result);
    
    return True

run_flag = True
while run_flag:
    welcome()
    run_flag = run_calculator()
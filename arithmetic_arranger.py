import re

supported_operators: str = "+-"
max_number_of_problems: int = 5
max_digits_per_operand: int = 4
number_of_operands_per_problem: int = 2

# Suppose e only have flat problem with no parenthesis and only +, or -, the total number of elements (operands
# and operator) is as below:
number_of_operands_and_operators: int = (number_of_operands_per_problem * 2) - 1


def get_operands_and_operator(problem: str):
    # global number_of_operands_and_operators
    elements = problem.split()

    # Checking the total number of operands + operator
    if len(elements) != number_of_operands_and_operators:
        print("Error: \"", problem, "\" doesn't comply with",
              number_of_operands_and_operators, "total number of operands and operator")
        quit()

    return elements


def check_format(problems: list[str]):
    # global max_digits_per_operand

    # Make sure we don't have too many problems supplied.
    if len(problems) > max_number_of_problems:
        print("Error: Too many problems.")
        quit()

    # Make sure only appropriate operators are used.
    for problem in problems:
        elements = get_operands_and_operator(problem)

        # If we reached here then we are sure we don't have any problem with the number of element in the problems.
        # We extract first_operand, operator, and second_operand.
        first_operand, operator, second_operand = [elements[e] for e in range(number_of_operands_and_operators)]

        # Checking the operator and making sure it's supported.
        if len(operator) != 1 or operator not in supported_operators:
            print("Error: Operator must be '+' or '-'.")
            quit()

        # Extra check: make sure actually have only digits in the operands
        pattern = "[0-9]+"
        if re.fullmatch(pattern, first_operand) is None or re.fullmatch(pattern, second_operand) is None:
            print("Error: Numbers must only contain digits.")
            print(first_operand, second_operand)
            quit()

        # Making sure each operand has a max of four digits in width
        if len(first_operand) > max_digits_per_operand or len(second_operand) > max_digits_per_operand:
            print("Error: Numbers cannot be more than four digits.")
            quit()


def compute(problems: list[str]):
    pass


def arrange(problems: list[str]):
    pass


def display_arrangement(problems: list[list[str]]):
    pass


def arithmetic_arranger(problems: list[str], compute=False):
    check_format(problems)

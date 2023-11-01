import re
import sys

supported_operators: str = "+-"
max_number_of_problems: int = 5
max_digits_per_operand: int = 4
number_of_operands_per_problem: int = 2

# Suppose we only have flat problem with no parenthesis and only +, or -, the total number of elements (operands
# and operator) is as below:
number_of_operands_and_operators: int = (number_of_operands_per_problem * 2) - 1


def get_operands_and_operator(problem: str) -> list[str]:
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


def arrange(problems: list[str], with_answers=False) -> list[list[str]]:
    """
    Sample arrangement with answers:
          32         1      9999      523
        +  8    - 3801    + 9999    -  49
        ----    ------    ------    -----
          40     -3800     19998      474

    Sample arrangement WITHOUT answers:
           32      3801      45      123
        + 698    -    2    + 43    +  49
        -----    ------    ----    -----
    """

    underline_character = "-"
    arrangement = list()

    line_1 = list()  # Operand 1
    line_2 = list()  # Operator
    line_3 = list()  # Operand 2
    line_4 = list()  # Answer (optional)

    block_seperator = "    "

    iteration = 0
    for problem in problems:
        elements = get_operands_and_operator(problem)

        # Add separators if iteration > 0, meaning we previously added some element,
        # so we add a separator before adding new elements.
        if iteration > 0:
            line_1.append(block_seperator)
            line_2.append(block_seperator)
            line_3.append(block_seperator)
            if len(line_4) > 0:  # Only process line_4 (answers) if data had been added previously.
                line_4.append(block_seperator)

        first_operand, operator, second_operand = [elements[e] for e in range(number_of_operands_and_operators)]

        # Determine the width of the problem arrangement which is
        # the maximum length of the operands + 2 (the space and the operator)
        width = max(len(first_operand), len(second_operand)) + 2

        # We start the justification to the right.
        formatted_first_line = str.rjust(first_operand, width)
        formatted_second_line = str.rjust(second_operand, width - 1)  # Minus 1 to create place for the operator
        formatted_second_line = operator + formatted_second_line
        formatted_third_line = str.rjust("", width, underline_character)

        # Prepare the arrangement line per line
        line_1.append(formatted_first_line)
        line_2.append(formatted_second_line)
        line_3.append(formatted_third_line)

        # Optionally add the answer
        if with_answers:
            formatted_fourth_line = str.rjust(str(eval(problem)), width)
            line_4.append(formatted_fourth_line)

        iteration += 1

    # Add the whole arrangement line by line.
    for line in line_1, line_2, line_3:
        arrangement.append(line)
    if with_answers:
        arrangement.append(line_4)

    return arrangement


def display_arrangement(problems: list[str], with_answers=False) -> None:
    arrangement = arrange(problems, with_answers)

    for line in arrangement:
        for element in line:
            sys.stdout.write(element)
        print()


def arithmetic_arranger(problems: list[str], with_answers=False) -> None:
    # First check the format and exit if syntax is incorrect.
    check_format(problems)

    # If we reach here without the program quitting, that means there was no syntax error.
    # So we proceed with arranging and displaying.
    if with_answers:
        display_arrangement(problems, with_answers)
    else:
        display_arrangement(problems)

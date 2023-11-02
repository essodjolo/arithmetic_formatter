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


def process_problems(problems: list[str], with_answers=False) -> str:
    """
    Checks if the problems are well formatted.
    Returns True if the format is okay.
    Returns Error message if an error found.
    """

    # Make sure we don't have too many problems supplied.
    if len(problems) > max_number_of_problems:
        return "Error: Too many problems."

    # Make sure only appropriate operators are used.
    for problem in problems:
        elements = get_operands_and_operator(problem)

        # If we reached here then we are sure we don't have any problem with the number of element in the problems.
        # We extract first_operand, operator, and second_operand.
        first_operand, operator, second_operand = [elements[e] for e in range(number_of_operands_and_operators)]

        # Checking the operator and making sure it's supported.
        if len(operator) != 1 or operator not in supported_operators:
            return "Error: Operator must be '+' or '-'."

        # Extra check: make sure actually have only digits in the operands
        pattern = "[0-9]+"
        if re.fullmatch(pattern, first_operand) is None or re.fullmatch(pattern, second_operand) is None:
            return "Error: Numbers must only contain digits."

        # Making sure each operand has a max of four digits in width
        if len(first_operand) > max_digits_per_operand or len(second_operand) > max_digits_per_operand:
            return "Error: Numbers cannot be more than four digits."

    return arrange(problems, with_answers)


def arrange(problems: list[str], with_answers=False) -> str:
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
    arrangement = ""

    line_1 = ""  # For first operands
    line_2 = ""  # For operators
    line_3 = ""  # For second operands
    line_4 = ""  # For answers (optional)

    block_seperator = "    "

    iteration = 0
    for problem in problems:
        elements = get_operands_and_operator(problem)

        # Add separators if iteration > 0, meaning we previously added some element,
        # so we add a separator before adding new elements.
        if 0 < iteration < len(problems):
            line_1 += block_seperator
            line_2 += block_seperator
            line_3 += block_seperator
            if len(line_4) > 0:  # Only process line_4 (answers) if data had been added previously.
                line_4 += block_seperator

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
        line_1 += formatted_first_line
        line_2 += formatted_second_line
        line_3 += formatted_third_line

        # Optionally add the answer
        if with_answers:
            formatted_fourth_line = str.rjust(str(eval(problem)), width)
            line_4 += formatted_fourth_line

        iteration += 1

    # Add the whole arrangement line by line.
    arrangement = line_1 + "\n" + line_2 + "\n" + line_3
    if with_answers:
        arrangement += "\n" + line_4

    return arrangement


def display_arrangement(problems: list[str], with_answers=False) -> None:
    arrangement = arrange(problems, with_answers)

    for line in arrangement:
        for element in line:
            sys.stdout.write(element)
        print()


def arithmetic_arranger(problems: list[str], with_answers=False) -> str:
    # First check the format and exit if syntax is incorrect.
    return process_problems(problems, with_answers)

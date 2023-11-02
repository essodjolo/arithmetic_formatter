import arithmetic_arranger as aa
import test_module

if __name__ == '__main__':
    # Perform unit tests first
    print("Perform unit tests first...")

    exec("test_module")

    testing = test_module.MyTestCase()

    testing.test_well_formatted_problems()
    testing.test_too_many_problems()
    testing.test_wrong_operator()
    testing.test_operands_with_non_digit_characters()
    testing.test_operands_with_more_than_4_digits()

    # Testing the examples given in the exercise to see if I get the same outputs
    print("No error during unit tests. Showing some examples of outputs...")

    # Example #1
    print("\nExample #1:")
    problems = ["32 + 698", "3801 + 2", "45 + 43", "123 + 49"]
    print(problems)
    print(aa.arithmetic_arranger(problems))

    # Example #2
    print("\nExample #2:")
    problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
    print(problems)
    print(aa.arithmetic_arranger(problems, True))


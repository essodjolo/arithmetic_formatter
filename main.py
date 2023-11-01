import arithmetic_arranger as aa

if __name__ == '__main__':
    # Testing the examples given in the exercise to see if I get the same outputs

    # Example #1
    problems = ["32 + 698", "3801 + 2", "45 + 43", "123 + 49"]
    print(problems)
    aa.arithmetic_arranger(problems)

    # Example #2
    problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
    print(problems)
    aa.arithmetic_arranger(problems, True)

import unittest
import arithmetic_arranger


class MyTestCase(unittest.TestCase):
    def test_well_formatted_problems(self):
        given_data = ['32 + 698', '3801 + 2', '45 + 43', '123 + 49']
        expected_result = '''   32      3801      45      123
+ 698    +    2    + 43    +  49
-----    ------    ----    -----'''
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

    def test_well_formatted_problems_with_answers(self):
        given_data = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
        expected_result = '''  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474'''
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data, True), expected_result)

    def test_too_many_problems(self):
        given_data = ['32 + 698', '3801 + 2', '45 + 43', '123 + 49', '3801 + 2', '45 + 43', '123 + 49']
        expected_result = 'Error: Too many problems.'
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

    def test_wrong_operator(self):
        expected_result = "Error: Operator must be '+' or '-'."

        given_data = ['32 + 698', '3801 d 2', '45 + 43']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

        given_data = ['32 ++ 698', '3801 - 2', '45 + 43']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

        given_data = ['32 * 698', '3801 - 2', '45 + 43']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

        given_data = ['32 + 698', '3801 - 2', '45 / 43']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

    def test_operands_with_non_digit_characters(self):
        expected_result = "Error: Numbers must only contain digits."

        given_data = ['a32 + 698']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

        given_data = ['32 + 698z']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

        given_data = ['aa + xyz']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

    def test_operands_with_more_than_4_digits(self):
        expected_result = "Error: Numbers cannot be more than four digits."

        given_data = ['11132 + 698']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

        given_data = ['32 + 69111']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)

        given_data = ['12345 + 678901']
        self.assertEqual(arithmetic_arranger.arithmetic_arranger(given_data), expected_result)


if __name__ == '__main__':
    unittest.main()

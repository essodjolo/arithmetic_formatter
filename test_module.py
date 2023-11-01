import unittest
import arithmetic_arranger


class MyTestCase(unittest.TestCase):
    def test_get_operands_and_operator(self):
        given_data = arithmetic_arranger.get_operands_and_operator("32 + 8")
        expected_result = ["32", "+", "8"]
        self.assertEqual(given_data, expected_result)  # add assertion here

    def test_arithmetic_arranger(self):
        given_data = arithmetic_arranger.arrange(["32 + 698", "3801 - 2"])
        expected_result = [["   32", "    ", "  3801"], ["+ 698", "    ", "-    2"], ["-----", "    ", "------"]]
        self.assertEqual(given_data, expected_result)


if __name__ == '__main__':
    unittest.main()

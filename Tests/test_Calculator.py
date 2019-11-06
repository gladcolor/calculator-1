import unittest
import math

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        # print("Start test_subtraction...")
        test_data = CsvReader(r"../Tests/Data/Unit Test Subtraction.csv").data
        # print(test_data)
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_divide(self):
        # print("Start test_subtraction...")
        test_data = CsvReader(r"../Tests/Data/Unit Test Division.csv").data
        # print(test_data)
        for row in test_data:
            result = float(row['Result'])
            len_deci = len(str(result).split(".")[1])
            result = round(result, len_deci)
            # print('len_deci: ', len_deci)
            self.assertEqual(round(self.calculator.divide(row['Value 1'], row['Value 2']), len_deci), result)
            self.assertEqual(round(self.calculator.result, len_deci), result)

    def test_add(self):
        # print("Start test_subtraction...")
        test_data = CsvReader(r"../Tests/Data/Unit Test Addition.csv").data
        # print(test_data)
        for row in test_data:
            result = float(row['Result'])
            len_deci = len(str(result).split(".")[1])
            result = round(result, len_deci)
            # print('len_deci: ', len_deci)
            self.assertEqual(round(self.calculator.add(row['Value 1'], row['Value 2']), len_deci), result)
            self.assertEqual(round(self.calculator.result, len_deci), result)

    def test_multiply(self):
        # print("Start test_subtraction...")
        test_data = CsvReader(r"../Tests/Data/Unit Test Multiplication.csv").data
        # print(test_data)
        for row in test_data:
            result = float(row['Result'])
            len_deci = len(str(result).split(".")[1])
            result = round(result, len_deci)
            # print('len_deci: ', len_deci)
            self.assertEqual(round(self.calculator.add(row['Value 1'], row['Value 2']), len_deci), result)
            self.assertEqual(round(self.calculator.result, len_deci), result)

if __name__ == '__main__':
    unittest.main()
"""
 ===============================================================
 test_module.py
 ===============================================================

 This module file is used to test the function.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-16
 Version : 0.5.0
"""

import unittest
import mean_var_std

class CalculatorTests(unittest.TestCase):
    """
     A test suit to group the unit tests to check if
     the function works correctly.
    """

    def test_calculate_with_few_digits(self) -> None:
        """
         Unit test for to check exception raising.
        """

        self.assertRaisesRegex(
            ValueError,
            "List must contain nine numbers.",
            mean_var_std.calculate,
            [2, 6, 2, 8, 4, 0, 1]
        )

if __name__ == "__main__":
    unittest.main()

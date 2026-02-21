"""
 ===============================================================
 main.py
 ===============================================================

 This entrypoint file is to be used in development
 for testing purposes.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-16
 Version : 1.0.0
"""

from unittest import main
import mean_var_std

# Testing the function here
print(mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Running unit tests automatically
main(module="test_module", exit=False)

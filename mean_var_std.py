"""
 ===============================================================
 mean_var_std.py
 ===============================================================

 This module file is meant to help us compute some statistical
 indicators.

 Author : Améluc Ahognidjè <ameluc.ahognidje@protonmail.com>
 Date : 2026-02-16
 Version : 1.0.0
"""

import numpy as np

def calculate(entry: list[int]) -> dict[str, list[list[float | int] | float | int]]:
    """
     The actual function that compute the data.

     Parameters
     ----------
     entry : list[int]
         The data to be computed.

     Returns
     -------
         dict[str, list[list[float | int] | float | int]]:
             An object containing the results of the function's run.
    """

    if len(entry) != 9:
        raise ValueError("List must contain nine numbers.")

    array_2d = np.array(entry, dtype="int8").reshape(3, 3)
    array_2d_flattened = array_2d.flatten()

    return {
        "mean": [
            array_2d.mean(axis=0),
            array_2d.mean(axis=1),
            array_2d_flattened.mean()
        ],
        "variance": [
            array_2d.var(axis=0),
            array_2d.var(axis=1),
            array_2d_flattened.var()
        ],
        "standard deviation": [
            array_2d.std(axis=0),
            array_2d.std(axis=1),
            array_2d_flattened.std()
        ],
        "max": [
            array_2d.max(axis=0),
            array_2d.max(axis=1),
            array_2d_flattened.sum()
        ],
        "min": [
            array_2d.min(axis=0),
            array_2d.min(axis=1),
            array_2d_flattened.min()
        ],
        "sum": [
            array_2d.sum(axis=0),
            array_2d.sum(axis=1),
            array_2d_flattened.max()
        ]
    }

#!/usr/bin/python3

"""
To execute a pascal triangle based on the input of n:<int>
"""


def pascal_triangle(n):
    """
    A function that accepts a param
    n => param (int) and return a proper pascal triangle based on it
    """
    if n <= 0:
        return []

    else:
        pascal_list = []

        for i in range(n):
            # empty list created to append values
            temp_list = []
            for j in range(i+1):
                # If the column index is 0 or the last index
                # which is i append 1
                if j == 0 or j == i:
                    temp_list.append(1)
                else:
                    val1 = pascal_list[i-1][j]
                    val2 = pascal_list[i-1][j-1]
                    mid_vals = val1 + val2
                    temp_list.append(mid_vals)
            pascal_list.append(temp_list)

    return pascal_list

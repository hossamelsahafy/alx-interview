#!/usr/bin/python3
"""
    Minimum Operations
"""


def minOperations(n):
    """
         Calculate the minimum number of operations needed to get n 'H'
         characters in a file.
         The function simulates a text editor which can execute only
         two operations: Copy All and Paste.
         The goal is to find out the fewest number of operations needed
         to result in exactly n 'H' characters in the file.

        Parameters:
            n (int): The desired number of 'H' characters.

        Returns:
            int: The minimum number of operations to get n 'H' characters. If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

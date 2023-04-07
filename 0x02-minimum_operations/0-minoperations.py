#!/usr/bin/python3
"""
This is a 2 key keyboard problem.
"""


def minOperations(n):
    """
    Given:
        Current number: n
        Returns: minimum number of operations
                Otherwise 0, if impossible to generate n H char
    """
    # Initialize the variables current, count, buffer1 to run dynamic
    current = 1  # current number of characters in the file
    count = 0  # minimum number of operations required
    buffer1 = 0  # number of characters to copy in a single operation

    # Continue until the number of characters in the file is equal to n
    while current < n:
        rest = n - current

        # Check if we can generate a sequence of H characters with the current
        # buffer1
        if(rest % current == 0):
            buffer1 = current
            current += buffer1  # copy and paste buffer1  number of characters
            count += 2  # two operations (copy and paste operation) performed

        else:
            current += buffer1  # paste buffer1 number of charactes
            count += 1  # one operation (paste) perfomed

    # Check if the resulting number of characters in the file is equal to n
    if current == n:
        return count  # return minimum number of operations required
    else:
        return 0  # return 0 if it is impossible to achieve n H characters

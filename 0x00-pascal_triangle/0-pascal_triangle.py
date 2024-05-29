#!/usr/bin/python3
"""
function  that returns a list of lists of
integers representing the Pascal's triangle of n
"""
def pascal_triangle(n):
    if (n <= 0):
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        L_row = triangle[i - 1]
        row += [sum(p) for p in zip(L_row, L_row[1:])]
        row.append(1)
        triangle.append(row)
    return triangle

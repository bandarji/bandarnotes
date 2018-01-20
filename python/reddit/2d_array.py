from pprint import pprint as pretty
from random import choice as choose

matrix_dimension = 10
matrix = [
    [
        choose([-1, 0, 1])
        for x in range(matrix_dimension)
    ] 
    for z in range(matrix_dimension)]

pretty(matrix)
[[0, 1, 0, -1, 1, 1, 0, 0, 1, -1],
[1, 0, 1, -1, 0, 0, 0, -1, 0, 0],
[-1, 0, -1, -1, -1, 1, 0, -1, 0, 0],
[-1, -1, 1, 1, 0, -1, 0, 0, 0, 0],
[1, 0, 0, -1, 1, 0, 0, 1, -1, 1],
[-1, -1, 0, 1, 1, 1, 1, 1, 1, -1],
[1, 1, 1, 0, -1, -1, -1, -1, 0, 0],
[1, 1, 0, -1, 1, 1, 0, 0, 0, 1],
[-1, 1, 1, 0, -1, -1, 0, -1, 0, 1],
[0, -1, -1, -1, 0, -1, -1, 0, 1, -1]]

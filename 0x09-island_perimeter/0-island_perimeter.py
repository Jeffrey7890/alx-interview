#!/usr/bin/python3


""" Island perimeter implementations """


def safe_check(grid, row, col):
    """ helper function for safety check """
    if row < 0 or col < 0:
        return True
    if row >= len(grid) or col >= len(grid[0]):
        return True
    if grid[row][col] == 1:
        return False
    return True


def island_perimeter(grid):
    """ island perimeter solution """
    row = len(grid)
    col = len(grid[0])
    cnt = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                # check for permiter
                if safe_check(grid, i - 1, j):
                    cnt += 1
                if safe_check(grid, i, j + 1):
                    cnt += 1
                if safe_check(grid, i + 1, j):
                    cnt += 1
                if safe_check(grid, i, j - 1):
                    cnt += 1
    return cnt

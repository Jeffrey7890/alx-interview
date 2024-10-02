#!/usr/bin/python3

""" implement factorial of number """

def factorial(n):
    """ Get factorial of number """
    if n == 0:
        return (1);
    return n * factorial(n-1)

def combination(n, k):
    """ Get combination of number """
    return (factorial(n)//(factorial(k)*factorial(n-k)))

def pascal_triangle(n):
    """ Pascals triangle """
    return [[combination(i,j) for j in range(i+1)] for i in range(n)]


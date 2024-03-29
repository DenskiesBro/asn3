# CMPT 145 Course material
# Copyright (C) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#    SOme functions to test.


def newtonraphson(x):
    """
    Purpose:
        To compute the square root of a given integer
    Pre-Conditions:
        An integer, x
    Post-Conditions:
        None
    Return:
        The root of the integer
    """

    root = 1
    while abs(x - root * root) > 0.00001:
        root = (x/root + root) / 2.0
    return root
 
def gcd(a, b):
    """
    Purpose:
        To compute the greatest divisor of two inputted integers
    Pre-conditions:
        Two integers, a and b
    Post-Conditions:

    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def read_triangle(filename):
    """
    Purpose: To read a Pascal triangle into a list and print out its size and the triangle itself


    """
    file = open(filename)
    triangle = []
    for line in file:
        line = line.rstrip().split()
        line = [int(d) for d in line]
        triangle.append(line)
    file.close()
    size = triangle[0][0]
    triangle = triangle[1:]

    return size, triangle


def remdup(alist):
    """ Add the doc-string! """
    alist.reverse()
    for i in range(len(alist)-1):
        while alist[i] in alist[i+1:]:
            del alist[i]
    alist.reverse()
    return alist


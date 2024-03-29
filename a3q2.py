# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    S debugging exercise, relevant to Chapter 3 and 7

def copy1(data):
    """
    Returns a copy of the given list of data
    Preconditions:
        :param data: a list
    Return:
        a copy of the given data
    """
    copied = data
    return copied

def copy2(data):
    """
    Returns a copy of the given list of data
    Preconditions:
        :param data: a list
    Return:
        a copy of the given data
    """
    copied = []
    for i in range(len(data)):
        copied.append(i)
    return copied


def copy3(data):
    """
    Copies the given list of data.
    Preconditions:
        :param data: a list
        :param copy: a list with the same contents as data
    Postconditions:
        data becomes empty
    :return: A copy of the list
    """
    copied = []
    for i in range(len(data)):
        d = data[i]
        data.remove(d)
        copied.append(d)
    return copied


def copy4(data, copy):
    """
    Copies the given list of data.
    Preconditions:
        :param data: a list
        :param copy: an empty list
    Post-conditions:
        copy has the same contents as data
    :return: None
    """
    copy = list()
    for d in data:
        copy.append(d)

    return None


def copy5(data, copy):
    """
    Copies values from data to the empty list copy
    Preconditions:
        :param data: a list
    Post-conditions:
        copy has the same contents as data
    Return:
        None
    """
    for d in data:
        copy = copy + [d]
    return None


def selection_sort(unsorted):
    """
    Returns a list with the same values as unsorted,
    but reorganized to be in increasing order.
    :param unsorted: a list of comparable data values
    :return:  a sorted list of the data values
    """

    result = list()

    # TODO use one of the copy() functions here

    while len(unsorted) > 0:
        out = min(unsorted)
        unsorted.remove(out)
        result.append(out)

    return result

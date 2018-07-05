import os
assert True == True

def mean(num_list):
    assert isinstance(num_list, list)
    return sum(num_list)/len(num_list)

from math import isclose
assert isclose(1.9999, 2, abs_tol=0.003)

def mean(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError as detail:
        msg = "The algebraic mean of an empty list is undefined. \
                    Please provide a list of numbers"
        raise ZeroDivisionError(detail.__str__() + "\n" + msg)

        
    

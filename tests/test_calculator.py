'''My Calculator Test'''
# Importing add and subtract functions from the calculator module
from calculator import add, subtract

def test_addition():
    '''Test that addition function works'''    
    assert add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works'''    
    assert subtract(2, 2) == 0

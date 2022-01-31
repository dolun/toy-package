####
import numpy as np
import pylab as pl

def get_array_shape(a)->tuple:
    """return the shape of an array

    Args:
        a (ndarray): input array
    Returns:
        tuple: shape of the array

    >>> get_array_shape(pl.randn(2,3,4))
    (2, 3, 4)
    """
    return a.shape

def is_it_number(in_value):
    """Checks if a value is a valid number.

    Parameters
    ----------
    in_value
        A variable of any type that we want to check is a number.

    Returns
    -------
    bool
        True/False depending on whether it was a number.

    Examples
    --------
    >>> is_it_number(1)
    True
    >>> is_it_number(1.0)
    True
    >>> is_it_number("1")
    True
    >>> is_it_number("1.0")
    True
    >>> is_it_number("Hello")
    False

    You can also pass more complex objects, these will all be `False`.

    >>> is_it_number({"hello": "world"})
    False
    >>> from datetime import datetime
    >>> is_it_number(datetime.now())
    False

    Even something which contains all numbers will be ``False``, because it is not itself a number.

    >>> is_it_number([1, 2, 3, 4])
    False

    """
    try:
        float(in_value)
        return True
    except (ValueError, TypeError):
        return False


def add_numbers(a, b):
    """Sums the given numbers.

    :param int a: The first number.
    :param int b: The second number.

    :return: The sum of the given numbers.

    >>> add_numbers(1, 2)
    3
    >>> add_numbers(50, -8)
    42
    """
    return a + b

def is_float(in_value):
    """Checks if a value is a valid float.

    Parameters
    ----------
    in_value
        A variable of any type that we want to check is a float.

    Returns
    -------
    bool
        True/False depending on whether it was a float.

    Examples
    --------
    >>> is_float(1.5)
    True
    >>> is_float(1)
    False

    """
    
    
    try:
        return not float(in_value).is_integer()
    except (ValueError, TypeError):
        return False



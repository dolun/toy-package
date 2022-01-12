from is_number import is_it_number, is_float
from datetime import datetime
import unittest


def test_is_number():
    assert is_it_number(1)


def test_is_not_number():
    assert not is_it_number("Hello world")
    assert not is_it_number({"Hello": "world"})


def test_is_float():
    assert is_float(1.1)

    assert not is_float(1)
    assert not is_float(1.0)
    assert not is_float("Hello world")
    assert not is_float({"Hello": "world"})
    assert not is_float(datetime.now())
    assert not is_float(lambda foo: foo)

# $ pytest <--doctest-modules>

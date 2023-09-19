import pytest
from lib.present import *

def test_wrap_then_unwrap():
    present = Present()
    present.wrap("Banana")
    assert present.unwrap() == "Banana"

def test_unwrap_without_contents():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

def test_wrap_without_unwrap():
    present = Present()
    present.wrap("dog")
    with pytest.raises(Exception) as err:
        present.wrap("cat")
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

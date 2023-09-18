from lib.greet import *

def test_greet_Bernie():
    result = greet("Bernie")
    assert result == "Hello, Bernie!"
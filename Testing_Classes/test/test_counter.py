from lib.counter import *

def test_add_one_digit_number():
    counter = Counter()
    counter.add(5)
    assert counter.report() == 'Counted to 5 so far.'
    
def test_add_negative_number():
    counter = Counter()
    counter.add(-3)
    assert counter.report() == 'Counted to -3 so far.'

def test_add_multiple_numbers():
    counter = Counter()
    counter.add(7)
    counter.add(11)
    counter.add(-2)
    assert counter.report() == 'Counted to 16 so far.'
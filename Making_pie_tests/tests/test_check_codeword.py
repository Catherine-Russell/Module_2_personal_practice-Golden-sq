from lib.check_codeword import *

def test_codeword_is_correct():
    response = check_codeword("horse")
    assert response == "Correct! Come in."

def test_codeword_is_close():
    response = check_codeword("hermione")
    assert response == "Close, but nope."

def test_mistakenly_close_keyword():
    response = check_codeword("hermiown")
    assert response == "WRONG!"

def test_codeword_is_incorrect():
    response = check_codeword("Wombles")
    assert response == "WRONG!"

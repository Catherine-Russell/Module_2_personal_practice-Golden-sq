import pytest
from lib.password_checker import *

def test_valid_password():
    pword_chk = PasswordChecker()
    assert pword_chk.check("C@ther1ne") == True

def test_all_whitespace():
    pwrd_chk = PasswordChecker()
    with pytest.raises(Exception) as err:
        pwrd_chk.check("          ")
    error_message = str(err.value)
    assert error_message == "Password cannot be empty space."

def test_too_short():
    pwrd_chk = PasswordChecker()
    with pytest.raises(Exception) as e:
        pwrd_chk.check("T0m£")
    err_msg = str(e.value)
    assert err_msg == "Invalid password, must be 8+ characters."

def test_no_special_characters():
    pwrd_chk = PasswordChecker()
    with pytest.raises(Exception) as e:
        pwrd_chk.check("El1zabeth")
    error_message = str(e.value)
    assert error_message == "Password must contain a special character"

def test_requires_numbers_and_letters():
    pwdchk = PasswordChecker()
    with pytest.raises(Exception) as error:
        pwdchk.check("Catherine")
    errmsg = str(error.value)
    assert errmsg == "Password must contain letters and numbers"
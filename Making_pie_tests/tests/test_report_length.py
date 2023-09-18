from lib.report_length import *

def test_check_short_string():
    result = report_length("House")
    assert result == "This string was 5 characters long."

def test_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."

def test_string_with_whitespaces():
    result = report_length("     Hello     ")
    assert result == "This string was 15 characters long."
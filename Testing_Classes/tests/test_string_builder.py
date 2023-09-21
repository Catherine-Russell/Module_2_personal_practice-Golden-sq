from lib.string_builder import *

def test_length_one_string():
    stringbuilder = StringBuilder()
    stringbuilder.add('Hello')
    length = stringbuilder.size()
    assert length == 5

def test_output_one_string():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hello")
    mystring = stringbuilder.output()
    assert mystring == 'Hello'

def test_add_multiple_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add('Hello')
    stringbuilder.add(' Catherine')
    stringbuilder.add(' and')
    stringbuilder.add(' Hilary.')
    assert stringbuilder.size() == 27

def test_add_multiple_strings_output():
    stringbuilder = StringBuilder()
    stringbuilder.add('Hello')
    stringbuilder.add(' Catherine')
    stringbuilder.add(' and')
    stringbuilder.add(' Hilary.')
    assert stringbuilder.output() == 'Hello Catherine and Hilary.'
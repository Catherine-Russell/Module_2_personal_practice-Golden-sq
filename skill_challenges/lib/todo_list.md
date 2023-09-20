1. Describe the problem:
    As a user
    So that I can keep track of my tasks
    I want to check if a text includes the string #TODO.
    just any random text which has todo? Does it need the #?
    What if its a paragraph?
    just a string?
    should it be 'TODO' or is todo ok? Is to do ok? To Do?
    What if within a word? Should it be " to do "? --> e.g. we're going to dot's house = false positive
    Does it need to be at the beginning of the string??


2. def check_if_todo()
    parameters = string of text
    returns True or False
    could it print the to do section of it? (unnecessary upgrade)

3. Tests
    - Given a string commencing in 'TODO', returns True TODO: clean the bathroom
    - Given a string commencing in "To do" returns True
    - Given a string commencing in 'todo' returns True
    - Given a string commencing in To Do returns True
    - Given a string with multiple sentences which contains Todo in second sentece, return True
    - Given a string with no todo in at all, return false
    - Given a string with multiple sentences but no todo, return False 
    - given a string with todo as part of a word returns False "I have a pet pentodon"
    - Given a string with to do as part of a word returns False "we're going to dot's house"
    - Given an empty string, returns error message "text cannot be empty"

    - Given a string with Todo not at beginning of string... [what would this even look like??]
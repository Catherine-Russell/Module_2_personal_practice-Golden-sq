from lib.grammar_stats import *
# test with both cl and . returns tru

def test_sentence_with_cl_and_fs_returns_true():
    grammar_checker = GrammarStats()
    assert grammar_checker.check("Today is Wednesday.") == True

# tests with cl and ! returns true
def test_sentence_with_cl_and_exclam__mark_returns_true():
    grammar_checker = GrammarStats()
    assert grammar_checker.check("Today is Wednesday!") == True

# test with cl and ? returns true
def test_sentence_with_cl_and_q__mark_returns_true():
    grammar_checker = GrammarStats()
    assert grammar_checker.check("Today is Wednesday?") == True

# test with no cl but punc returns False
def test_sentence_with_punc_but_no_cl_returns_false():
    grammar_checker = GrammarStats()
    assert grammar_checker.check("today is Wednesday!") == False

# test with cl but no punc returns False
def test_sentence_with_cl_but_no_punc_returns_false():
    grammar_checker = GrammarStats()
    assert grammar_checker.check("Today is Wednesday") == False

# test with neither cl not punc returns False
def test_sentence_with_no_punc_or_cl_returns_false():
    grammar_checker = GrammarStats()
    assert grammar_checker.check("Today is Wednesday") == False

# test with wrond punc returns false
def test_sentence_with_wrong_punc_returns_false():
    grammar_checker = GrammarStats()
    assert grammar_checker.check("Today is Wednesday:") == False

# test which callse percentage after 1 correct sentence
def test_100_after_1_correct_sentence():
    grammar_checker = GrammarStats()
    grammar_checker.check("Today is Wednesday!")
    assert grammar_checker.percentage_good() == 100

# test which calls percentage after 1 incorrect sentence
def test_0_after_1_incorrect_sentence():
    grammar_checker = GrammarStats()
    grammar_checker.check("Today is Wednesday")
    assert grammar_checker.percentage_good() == 0

# test which callse percentage after 6 sentences - whol num percentage -mixture of incor and cor whole number
def test_6_qs_mixed_grade():
    grammar_checker = GrammarStats()
    grammar_checker.check("Today is Wednesday!")
    grammar_checker.check("today is Wednesday!")
    grammar_checker.check("Today is Wednesday")
    grammar_checker.check("Today is Wednesday?")
    grammar_checker.check("Today is Wednesday.")
    assert grammar_checker.percentage_good() == 60

# test which callse percentage after 3 sentences - decimal num percentage -mixture of incor and cor whole number
def test_percentage_is_whole_number():
    grammar_checker = GrammarStats()
    grammar_checker.check("Today is Wednesday!")
    grammar_checker.check("today is Wednesday!")
    grammar_checker.check("Today is Wednesday")

    assert grammar_checker.percentage_good() == 33
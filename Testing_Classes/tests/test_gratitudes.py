from lib.gratitudes import *

def test_add_and_return_1_gratitude():
    gratitudelst = Gratitudes()
    gratitudelst.add("family")
    assert gratitudelst.format() == "Be grateful for: family"

def test_add_and_return_2_gratitudes():
    gratitudelst = Gratitudes()
    gratitudelst.add("family")
    gratitudelst.add("friends")
    assert gratitudelst.format() == "Be grateful for: family, friends"


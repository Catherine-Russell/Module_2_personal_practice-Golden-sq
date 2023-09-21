import math
class GrammarStats:
    def __init__(self):
        self.number_answered = 0
        self.number_correct = 0

    def check(self, text):
        self.number_answered += 1
        if text[0].isupper() and text[-1] in ".!?":
            self.number_correct += 1
            print(f"{text} is correct so now I have answered {self.number_answered} qs and I have {self.number_correct} correct")
            return True
        else:
            print(f"{text} is incorrect so now I have answered {self.number_answered} qs and I have {self.number_correct} correct")
            return False


    def percentage_good(self):
        percent_correct = round((self.number_correct/self.number_answered)*100)
        return percent_correct




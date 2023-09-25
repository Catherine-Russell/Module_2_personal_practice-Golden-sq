import math
class DiaryEntry():
    def __init__(self, date, contents):
        self.date = date
        self.contents = contents

    def word_count(self):
        return len(self.date.split()) + len(self.contents.split())

    def reading_duration(self, wpm):
        wordcount = self.word_count()
        return math.ceil(wordcount/wpm)
    

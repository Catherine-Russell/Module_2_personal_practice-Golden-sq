import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entry cannot be an empty string")
        self.title = title
        self.contents = contents
        self.chunk_counter = 0
        self.read_count = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())

    def reading_time(self, wpm):
        word_count = self.count_words()
        return math.ceil(word_count/wpm)
        
    def reading_chunk(self, wpm, minutes):
        complete_entry = (self.title + ": " + self.contents).split()
        prev_read_count = self.read_count
        self.read_count = wpm*minutes
        if self.chunk_counter == 0:
            self.chunk_counter += 1
            chunk = " ".join(complete_entry[0:self.read_count])
            return chunk
        else:
            self.chunk_counter = 0
            chunk = " ". join(complete_entry[prev_read_count:(prev_read_count + self.read_count)])
            return chunk
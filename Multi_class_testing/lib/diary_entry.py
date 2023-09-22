class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_words = 0

    def count_words(self):
        return (len(self.title.split()) + len(self.contents.split()))

    def reading_time(self, wpm):
        length = self.count_words()
        duration = length/wpm
        return duration

    def reading_chunk(self, wpm, minutes):
        complete_entry = (f"{self.title}: {self.contents}").split()
        readable_words = wpm * minutes
        if self.read_words == 0:
            chunk = " ".join(complete_entry[: readable_words])
            self.read_words = readable_words
        else:
            chunk = " ".join(complete_entry[self.read_words: self.read_words+readable_words])
            self.read_words = 0
        return chunk

from lib.diary_entry import DiaryEntry
import math

class Diary:
    def __init__(self):
        self.entry_list = []

    def add(self, entry):
        self.entry_list.append(entry)

    def all(self):
        return self.entry_list

    def count_words(self):
        word_count = 0
        for entry in self.entry_list:
            word_count += entry.count_words()
        return word_count

    def reading_time(self, wpm):
        total_words = self.count_words()
        duration = math.ceil(total_words/wpm)
        return duration

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if len(self.entry_list) == 0:
            raise Exception("You currently have no entries")
        readable_words = wpm*minutes
        possible_entries =[entry for entry in self.entry_list if entry.count_words() <= readable_words]
        if len(possible_entries) == 0:
            raise Exception("You don't have any entries which are short enough to read")
        ordered_possible_entries = sorted(possible_entries, key=lambda entry:entry.count_words())
        return f"{ordered_possible_entries[-1].title}: {ordered_possible_entries[-1].contents}"
    
my_diary = Diary()
entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
entry2 = DiaryEntry("Tuesday 2nd January", "I have recovered from the hangover and went for a nice long walk along the beach.")
entry3 = DiaryEntry("Wednesday 3rd January 2023", "Today I ate sushi with Samir")
my_diary.add(entry1)
my_diary.add(entry2)
my_diary.add(entry3)
print(my_diary.find_best_entry_for_reading_time(5, 5))
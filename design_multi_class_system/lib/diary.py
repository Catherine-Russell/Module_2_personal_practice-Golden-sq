from lib.diary_entry import DiaryEntry
from lib.task import Task

class Diary():
    def __init__(self):
        self.past_entries = []
        self.todo_list = []
        self.contacts = []

    def add_diary_entry(self, entry):
        words = entry.contents.split()
        for word in words:
            if (len(word) == 11) and (word[0]=='0') and (word.isdigit()):
                self.contacts.append(word)
                print(word)
        self.past_entries.append(entry)

    def add_task(self, task):
        self.todo_list.append(task)

    def show_todo_list(self):
        completed_task = [i.details for i in self.todo_list if i.is_complete == False]
        return completed_task
    
    def show_contacts(self):
        print(self.contacts)
        return self.contacts
    
    def show_past_diary_entries(self):
        return self.past_entries

    def select_entry_when_busy(self, wpm, time):
        if len(self.past_entries) < 1:
            raise Exception("No entries to choose from!")
        else:
            readable_words = wpm*time
            readable_entries = []
            for entry in self.past_entries:
                if entry.word_count() <= readable_words:
                    readable_entries.append(entry)
            # readable_entries = [entry
            #                     for entry in self.past_entries
            #                     if entry.word_count() <= readable_words]
            sorted_entries = sorted(readable_entries, key=lambda entry:entry.word_count())
            return sorted_entries[-1]
diary = Diary()
entry1 = DiaryEntry("Monday 1st January", "Today I woke up tired and hungover. 07783123453")
diary.add_diary_entry(entry1)
diary.select_entry_when_busy(2, 10)

from lib.diary_entry import DiaryEntry

# 1. test make diary entry and call  the title and contents separately
def test_make_diary_entry_and_check_title_and_contents():
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    assert entry1.title == "Monday 1st January 2023"
    assert entry1.contents == "Today I woke up hungover and unhappy."

# 2. test make diary enry and call count words
def test_make_entry_and_count_words():
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy.")
    assert entry1.count_words() == 11

# 3. test make diary entry and call reading time
def test_make_entry_and_return_reading_time():
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy. What a way to ring in the new year, eh? I tried to assess my new years resolutions but, quite honestly, I'm too hungover.")
    assert entry1.count_words() == 35
    assert entry1.reading_time(7) == 5

# 4. test make diary and call reading chunk once
def test_call_reading_chunk_once():
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy. What a way to ring in the new year, eh? I tried to assess my new years resolutions but, quite honestly, I'm too hungover.")
    assert entry1.reading_chunk(5, 2) == "Monday 1st January 2023: Today I woke up hungover and"

# 5. test make diary and call reading chunk second time
def test_call_reading_chunk_twice():
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy. What a way to ring in the new year, eh? I tried to assess my new years resolutions but, quite honestly, I'm too hungover.")
    entry1.reading_chunk(5, 2)
    assert entry1.reading_chunk(5, 2) == "unhappy. What a way to ring in the new year,"

# 6. test make diary and call reading chunk third time

def test_call_reading_chunk_thrice():
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy. What a way to ring in the new year, eh? I tried to assess my new years resolutions but, quite honestly, I'm too hungover.")
    entry1.reading_chunk(5, 2)
    entry1.reading_chunk(5, 2)
    assert entry1.reading_chunk(5, 2) == "Monday 1st January 2023: Today I woke up hungover and"

# 7. test make diary and call reading chunk twice with different times and word counts
def test_call_reading_chunk_with_diff_durations_and_wpm():
    entry1 = DiaryEntry("Monday 1st January 2023", "Today I woke up hungover and unhappy. What a way to ring in the new year, eh? I tried to assess my new years resolutions but, quite honestly, I'm too hungover.")
    entry1.reading_chunk(5, 2)
    assert entry1.reading_chunk(7, 3) == "unhappy. What a way to ring in the new year, eh? I tried to assess my new years resolutions but, quite"
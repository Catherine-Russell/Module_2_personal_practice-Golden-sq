from lib.diary_entry_class import *
import pytest
from lib.diary_contents import *

# test whether title and contents have been saved appropriately
def test_title_saved_appropriately():
    my_diary = DiaryEntry("Wednesday 20th September", "Today has been a wet and windy day and I have a headache.")
    
    assert my_diary.title == "Wednesday 20th September"

def test_contents_saved_appropriately():
    my_diary = DiaryEntry("Wednesday 20th September", "Today has been a wet and windy day and I have a headache.")
    assert my_diary.contents == "Today has been a wet and windy day and I have a headache."

# test whether empty string (e.g. missing contents) returns error
def test_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        my_diary = DiaryEntry("", "It's bloody raining today ffs.")
    error_message = str(e.value)
    assert error_message == "Diary entry cannot be an empty string"


# test whether it comes out formatted

def test_title_and_contents_return_formatted():
    my_diary = DiaryEntry("Wednesday 20th September", "Today has been a wet and windy day and I have a headache.")
    assert my_diary.format() == "Wednesday 20th September: Today has been a wet and windy day and I have a headache."

# check word count - with short contents
def test_word_count_with_short_contents():
    my_diary = DiaryEntry("Wednesday 20th September", "Today has been a wet and windy day and I have a headache.")
    assert my_diary.count_words() == 16

# check word count - with multiple sentences

def test_word_count_with_long_contents():
    my_diary = DiaryEntry("Thursday 14th September 1993", diary_contents)
    assert my_diary.count_words() == 750


# check reading time - with whole num answer

def test_reading_time_with_whole_number_ans():
    my_diary = DiaryEntry("Thursday 14th September 1993", diary_contents)
    assert my_diary.reading_time(150) == 5

#  check reading time - with decimal ans turning to int

def test_reading_time_with_decimal_number_ans():
    my_diary = DiaryEntry("Thursday 14th September 1993", diary_contents)
    assert my_diary.reading_time(63) == 12

# reading chunk - first time called returns first x letters

def test_reading_chunk_first_call_gives_first_chunk():
    my_diary = DiaryEntry("Thursday 14th September 1993", diary_contents)
    chunk = my_diary.reading_chunk(60,3)
    assert chunk == "Thursday 14th September 1993: I am still in shock. Today has been one of the most overwhelming days of my life! Today was the day I learnt we are going to be moving to England. As I sit here, looking out over Kingston, my heart is beating a million miles an hour in anticipation as questions race through my mind: what will England be like? Will it be like Jamaica? Where will we live? Will we be able to find work? It all began when my husband arrived back in Jamaica having been discharged from the British Royal Air Force. He has served for two years and had been based in Oxford, which he described as a quaint, picturesque city. For the last two months, he has been rambling on about moving the whole family to England – he is SO enthusiastic, he will hardly chat about anything else! This morning he woke up particularly early seeing as he doesn’t have a job and rushed down to Kingston Harbour where there was a meeting for ex-service people. While he was"

# reading chunk called again returns next chunk along
def test_reading_chunk_second_call_gives_second_chunk():
    my_diary = DiaryEntry("Thursday 14th September 1993", diary_contents)
    my_diary.reading_chunk(60,3)
    chunk = my_diary.reading_chunk(60,3)
    assert chunk == "there, I cooked ackee and saltfish for the kids before I sent them off to their primary school.Throughout my shift in the hospital, I felt uneasy and when I returned home I was met with the news… He has bought tickets for us all to travel on a massive boat, which is departing from Kingston to England! As he told me the news, his eyes sparkled and his face was flushed with colour – he was, it seemed, ridiculously excited. When the children returned from school, we told them the news and we were met with screams of joy and what seemed like a million questions. I am excited too, but apprehensive about leaving my friends, my work and my sister. I suppose I’ll just put on a brave face for them even though I’m not sure how I feel! Sitting here now, three words are etched into my mind – ‘the Empire Windrush’. The words mean nothing to me, but represent the future, a new life and hopefully new life and hopefully better opportunities for us. Despite my stomach"


# reading chunk called a third time returns first chunk

def test_reading_chunk_third_call_gives_first_chunk():
    my_diary = DiaryEntry("Thursday 14th September 1993", diary_contents)
    my_diary.reading_chunk(60,3)
    my_diary.reading_chunk(60,3)
    chunk = my_diary.reading_chunk(60,3)
    assert chunk == "Thursday 14th September 1993: I am still in shock. Today has been one of the most overwhelming days of my life! Today was the day I learnt we are going to be moving to England. As I sit here, looking out over Kingston, my heart is beating a million miles an hour in anticipation as questions race through my mind: what will England be like? Will it be like Jamaica? Where will we live? Will we be able to find work? It all began when my husband arrived back in Jamaica having been discharged from the British Royal Air Force. He has served for two years and had been based in Oxford, which he described as a quaint, picturesque city. For the last two months, he has been rambling on about moving the whole family to England – he is SO enthusiastic, he will hardly chat about anything else! This morning he woke up particularly early seeing as he doesn’t have a job and rushed down to Kingston Harbour where there was a meeting for ex-service people. While he was"

def test_different_wpm_and_mins_for_both_times():
    my_diary = DiaryEntry("Thursday 14th September 1993", diary_contents)
    my_diary.reading_chunk(5,3)
    chunk = my_diary.reading_chunk(2,5)
    assert chunk == "most overwhelming days of my life! Today was the day"
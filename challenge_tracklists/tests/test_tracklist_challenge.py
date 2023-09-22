from lib.tracklist_challenge import *
import pytest

def test_none_added_returns_empty_list():
    my_tracker = MusicTracker()
    assert my_tracker.see_list() == []

def test_one_track_added():
    my_tracker = MusicTracker()
    my_tracker.add_track("Hit Me Baby One More Time")
    assert my_tracker.see_list() == ["Hit Me Baby One More Time"]

def test_two_tracks_added():
    my_tracker = MusicTracker()
    my_tracker.add_track("Hit Me Baby One More Time")
    my_tracker.add_track("It's Gonna Be Me")
    assert my_tracker.see_list() == ["Hit Me Baby One More Time", "It's Gonna Be Me"]

def test_add_list_of_tracks():
    my_tracker = MusicTracker()
    my_tracker.add_track(["Hit Me Baby One More Time", "It's Gonna Be Me", "Wannabe"])
    assert my_tracker.see_list() == ["Hit Me Baby One More Time", "It's Gonna Be Me", "Wannabe"]

def test_add_single_track_then_list_of_tracks():
    my_tracker = MusicTracker()
    my_tracker.add_track("Hit Me Baby One More Time")
    my_tracker.add_track(["It's Gonna Be Me", "Wannabe"])
    assert my_tracker.see_list() == ["Hit Me Baby One More Time", "It's Gonna Be Me", "Wannabe"]

def test_empty_string_raises_exception():
    my_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        my_tracker.add_track("")
    error_msg = str(e.value)
    assert error_msg == "Empty string cannot be added to tracklist"

def test_wrong_type_raises_exception():
    my_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        my_tracker.add_track(573)
    error_msg = str(e.value)
    assert error_msg == "Please input a string or list of strings"

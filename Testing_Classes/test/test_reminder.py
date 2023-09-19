import pytest
from lib.reminder import *

def test_reminds_user_to_do_task():
    reminder = Reminder("Catherine")
    reminder.remind_me_to("cook dinner")
    print(reminder.remind)
    result = reminder.remind
    result == "cook dinner, Catherine!"

def test_no_reminder_set():
    reminder = Reminder("Catherine")
    with pytest.raises(Exception) as err:
        reminder.remind()
    error_message = str(err.value)
    assert error_message == "No reminder set!"
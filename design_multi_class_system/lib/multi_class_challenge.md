1. Describe the problem
    As a user
    So that I can record my experiences
    I want to keep a regular diary

    As a user
    So that I can reflect on my experiences
    I want to read my past diary entries

    As a user
    So that I can reflect on my experiences in my busy day
    I want to select diary entries to read based on how much time I have and my reading speed

    As a user
    So that I can keep track of my tasks
    I want to keep a todo list along with my diary

    As a user
    So that I can keep track of my contacts
    I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the class system:

Nouns:
    diary
    diary entry
    reading speed
    todo list
    tasks
    contact
    mobile phone numbers

Verbs:
    record experiences
    reflect
    read
    select (based on reading speed and time)
    keep track (tasks)
    keep track (contacts)

3. Integration tests:
    - add diary entries and reflect on diary ==> [entry1, entry2, entry3]
    - add diary entries and select one for when busy ==> returns entry closest in time to read but without going over
    - add diary entries and select one for when busy ==> returns entry closest in time to read but without going over WHEN closest is just over
    - add contact and see contacts ==> {name1:number1, name2:number2}
    - add tasks and see in todo list ==> [task1, task2, task3]
    - add tasks, mark 1 complete and see todo list without that one ==> [task1, task3]
    - 

4. Unit tests:
    diary:
        - list todolist (empty)
        - list contacts before added returns empty dict
        - list reflects on before added returns empty list
        - select_diary_when_busy returns error when none added yet
    
    diary_entry:
        - make diary entry and check word count
        - make diary entry and return how long it will take to read (input wpm)

    task:
        - create a task amd call it
        - create a task and mark it complete
        - empty string returns err
        - non-string returns error

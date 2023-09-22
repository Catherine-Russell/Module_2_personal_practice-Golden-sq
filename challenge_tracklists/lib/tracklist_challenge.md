1. Describe the problem
    As a user
    So that I can keep track of my music listening
    I want to add tracks I've listened to and see a list of them.

2. Design class interface

class MusicTracker():

methods:
init
add tracks
see_list_of _listened


3. Tests
    <!-- - see list of empty tracks (none added yet) ==> [] -->
    <!-- - Add 1 track and call the list ["track1"] -->
    <!-- - Add 2 tracks and call the list ["track1", "track2"] -->
    <!-- - Add multiple tracks in a list ==> ["track1", "track2", "track3"] -->
    <!-- - Add 1 track then a list of tracks ==> ["track1", "track2", "track3"] -->

    Edge cases:
        <!-- - empty string raises exception "Empty string cannot be added to tracklist" -->
        - non-string or list track raises exception "Please input a string or list of strings"


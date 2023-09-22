class MusicTracker():
    def __init__(self):
        self.tracklist = []
    
    def add_track(self, track):
        if type(track) == str:
            if track == "":
                raise Exception("Empty string cannot be added to tracklist")
            else:
                self.tracklist.append(track)
        elif type(track) == list:
            self.tracklist.extend(track)
        else:
            raise Exception("Please input a string or list of strings")

    def see_list(self):
        return self.tracklist
import datetime

# Store the next available id for all new notes.
last_id = 0


class Note:
    def __init__(self, memo, tags=""):
        """
        Represent a note in the notebook. Match against a string
        in searches and store tags for each note.
        """
        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tags = tags
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """
        Determine if this note matches te filter text. Return true id it matces
        and return false if the filter does not match

        Search is case-sensitive and matches both text and tas
        """
        return filter in self.memo or filter in self.tags


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tag=""):
        self.notes.append(Note(memo, tag))

    def find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        note = self.find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False


    def modify_tags(self,note_id,tags):
        self.find_note(note_id).tags = tags

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

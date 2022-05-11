import pickle
class MuleManager():
    def __init__(self, characters=None):
        self.save_file_path = ''
        if (characters is None):
            self.characters = []
        else:
            self.characters = characters

    def save_path(self, sfp):
        self.save_file_path = sfp
        return self

    def add_character(self, character):
        self.characters.append(character)

    def num_characters(self):
        return len(self.characters)

    def save(self):
        with open(self.save_file_path, "wb") as file:
            pickle.dump(self.characters, file)

    def load(self):
        with open(self.save_file_path, "rb") as file:
            self.characters = pickle.load(file)

    def list_characters_with_indices(self):
        rstr = 'Characters: '
        for i in range(len(self.characters)):
            print(f'\n{i}.  {self.characters[i].character_name}')

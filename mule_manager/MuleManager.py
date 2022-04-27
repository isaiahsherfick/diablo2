class MuleManager():
    def __init__(self):
        self.save_file_path = ''

    def save_path(self, sfp):
        self.save_file_path = sfp
        return self

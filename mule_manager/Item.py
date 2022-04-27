import pickle
class Item():
    def __init__(self):
        self.item_name = "???"
        self.item_rolls = []
    def name(self, name):
        self.item_name = name
        return self
    def rolls(self, rollsList):
        l = [r for r in rollsList]
        self.item_rolls = l
        return self
    def __eq__(self, other):
        if (isinstance(other, Item)):
            return self.item_name == other.item_name and self.item_rolls == other.item_rolls
        else:
            return False

class Item:
    def __init__(self):
        self.item_name = "???"
        self.item_rolls = []
        self.inventory_space = 0

    def name(self, name):
        self.item_name = name
        return self

    def rolls(self, rollsList):
        l = [r for r in rollsList]
        self.item_rolls = l
        return self

    def space(self, tiles):
        self.inventory_space = tiles
        return self

    def __eq__(self, other):
        if (isinstance(other, Item)):
            return self.item_name == other.item_name
        else:
            return False

    def __str__(self):
        rstr = f"{self.item_name}"
        for roll in self.item_rolls:
            rstr += f'\n\t{roll}'
        return rstr

    def __gt__(self, other):
        if (isinstance(other, Item)):
            return self.inventory_space > other.inventory_space
        else:
            return False

    def __lt__(self, other):
        if (isinstance(other, Item)):
            return self.inventory_space < other.inventory_space
        else:
            return False

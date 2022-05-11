from Item import Item
from Gem import Gem
from Rune import Rune
class Character:
    def __init__(self):
        self.character_name = ""
        self.held_items = []
        self.held_runes = []
        self.held_gems = []
        self.inventory_size = 140

    def name(self, n):
        self.character_name = n
        return self

    def has_item(self, item_name):
        for item in self.held_items:
            if item.item_name == item_name:
                return True
        return False

    def has_rune(self, rune_name):
        for rune in self.held_runes:
            if rune.rune_name == rune_name:
                return True
        return False

    def has_gem(self, gem_name):
        for gem in self.held_gems:
            if gem.gem_name == gem_name:
                return True
        return False

    def add_item(self, item):
        if (isinstance(item, Item)):
            self.held_items.append(item)
            self.inventory_size -= item.inventory_space
        elif (isinstance(item, Rune)):
            self.held_runes.append(item)
            self.inventory_size -= 1
        elif (isinstance(item, Gem)):
            self.held_gems.append(item)
            self.inventory_size -= 1

    def get_inventory(self):
        inventory = []
        for i in range(len(self.held_items)):
            inventory += [self.held_items[i]]
        for i in range(len(self.held_runes)):
            inventory += [self.held_runes[i]]
        for i in range(len(self.held_gems)):
            inventory += [self.held_gems[i]]
        return inventory

    def list_inventory_with_indices(self):
        rstr = f'Items:'
        for i in range(len(self.held_items)):
            rstr+=f'\n\t{i}. {self.held_items[i].item_name}'
        rstr += f'\nRunes:'
        for i in range(len(self.held_runes)):
            rstr+=f'\n\t{i}. {self.held_runes[i]}'
        rstr += f'\nGems:'
        for i in range(len(self.held_gems)):
            rstr+=f'\n\t{i}. {self.held_gems[i]}'
        return rstr

    def remove_item_at(self, index):
        self.held_items.pop(index)

    def remove_rune_at(self, index):
        self.held_runes.pop(index)

    def remove_gem_at(self, index):
        self.held_gems.pop(index)

    def __str__(self):
        rstr = f'{self.character_name}:\t{len(self.held_items)} items\t{len(self.held_runes)} runes\t{len(self.held_gems)} gems\t{self.inventory_size} remaining inventory tiles'
        return rstr

    def __eq__(self, other):
        if (isinstance(other, Character)):
            my_inventory = self.get_inventory()
            their_inventory = other.get_inventory()
            if (len(my_inventory) == len(their_inventory)):
                for i in range(len(their_inventory)):
                    item = their_inventory[i]
                    for j in range(len(my_inventory)):
                        if (my_inventory[j] == item):
                            my_inventory.pop(j)
                            break
                return len(my_inventory) == 0
        return False

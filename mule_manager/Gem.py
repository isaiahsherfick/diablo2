import enum


class GemModifierOrder(enum.Enum):
    chipped = 1
    flawed = 2
    regular = 3
    flawless = 4
    perfect = 5


class Gem:
    def __init__(self):
        self.gem_class = ""
        self.gem_quality = ""
        self.quality_value = 0

    def gem_type(self, gclass):
        formatted_type = f"{gclass[0].upper()}{gclass[1:].lower()}"
        self.gem_class = formatted_type
        return self

    def quality(self, qual):
        self.gem_quality = qual
        for g in GemModifierOrder:
            if g.name == qual.lower():
                self.quality_value = g.value
        return self

    def __eq__(self, other):
        if (isinstance(other, Gem)):
            return self.gem_class == other.gem_class and self.quality_value == other.quality_value
        else:
            return False

    def __str__(self):
        rstr = f'{self.gem_quality} {self.gem_class}'
        return rstr

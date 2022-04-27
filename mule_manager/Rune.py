import enum


class RuneOrder(enum.Enum):
    El = 1
    Eld = 2
    Tir = 3
    Nef = 4
    Eth = 5
    Ith = 6
    Tal = 7
    Ral = 8
    Ort = 9
    Thul = 10
    Amn = 11
    Sol = 12
    Shael = 13
    Dol = 14
    Hel = 15
    Io = 16
    Lum = 17
    Ko = 18
    Fal = 19
    Lem = 20
    Pul = 21
    Um = 22
    Mal = 23
    Ist = 24
    Gul = 25
    Vex = 26
    Ohm = 27
    Lo = 28
    Sur = 29
    Ber = 30
    Jah = 31
    Cham = 32
    Zod = 33


class Rune():
    def __init__(self):
        self.rune_name = ''
        self.value = 0

    def name(self, name):
        formattedName = f"{name[0].upper()}{name[1:].lower()}"
        self.rune_name = formattedName
        for rune in RuneOrder:
            if rune.name == self.rune_name:
                self.value = rune.value
        return self

    def __eq__(self, other):
        if (isinstance(other, Rune)):
            return self.rune_name == other.rune_name
        else:
            return False
    def __lt__(self, other):
        if (isinstance(other, Rune)):
            return self.value < other.value
        else:
            return False
    def __gt__(self, other):
        if (isinstance(other, Rune)):
            return self.value > other.value
        else:
            return False

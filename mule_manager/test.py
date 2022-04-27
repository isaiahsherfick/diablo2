import unittest
from MuleManager import MuleManager
from Item import Item
from Rune import Rune
from Character import Character
from Gem import Gem


class MuleManagerTest(unittest.TestCase):
    def test_mm_instantiation(self):
        path = "/users/isaiah/.d2mm/save"
        mm = MuleManager().save_path(path)
        self.assertTrue(isinstance(mm, MuleManager))
        self.assertEqual(mm.save_file_path, path)

    def test_item_instantiation(self):
        soj = Item().name("The Stone Of Jordan").rolls(["+7 lightning damage"])
        self.assertEqual(soj.item_name, "The Stone Of Jordan")
        self.assertEqual(soj.item_rolls, ["+7 lightning damage"])

    def test_item_equals(self):
        soj = Item().name("The Stone Of Jordan").rolls(["+7 lightning damage"])
        soj2 = Item().name("The Stone Of Jordan").rolls(
            ["+7 lightning damage"])
        self.assertEqual(soj, soj2)

    def test_item_comparison(self):
        soj = Item().name("The Stone Of Jordan").space(1).rolls(["+7 lightning damage"])
        soj2 = Item().name("The Stone Of Jordan").rolls(
            ["+7 lightning damage"])
        iks_armor = Item().name("Immortal King's Armor").space(6)
        self.assertTrue(soj < iks_armor)

    def test_item_string(self):
        soj = Item().name("The Stone Of Jordan").rolls(["+7 lightning damage"])
        self.assertEqual(
            "The Stone Of Jordan\n\t+7 lightning damage",
            str(soj))
        anniRolls = [
            "+12 To All Attributes",
            "All Resistances +13",
            "+1-% To Experience Gained"]
        anniName = "Annihilus Small Charm"
        anni = Item().name(anniName).rolls(anniRolls)
        expected = f"{anniName}\n\t{anniRolls[0]}\n\t{anniRolls[1]}\n\t{anniRolls[2]}"
        self.assertEqual(str(anni), expected)

    def test_rune_instantiation(self):
        jah = Rune().name("jah")
        self.assertEqual(jah.rune_name, "Jah")
        self.assertEqual(jah.value, 31)
        ber = Rune().name("BER")
        self.assertEqual(ber.rune_name, "Ber")
        self.assertEqual(ber.value, 30)
        zod = Rune().name("Zod")
        self.assertEqual(zod.rune_name, "Zod")
        self.assertEqual(zod.value, 33)

    def test_rune_comparison(self):
        ist = Rune().name("Ist")
        jah = Rune().name("Jah")
        self.assertTrue(jah > ist)
        self.assertFalse(jah == ist)
        jah2 = Rune().name("JAH")
        self.assertEqual(jah, jah2)
        self.assertTrue(ist < jah2)

    def test_character_instantiation(self):
        mule = Character().name("Mule1")
        self.assertEqual(mule.character_name, "Mule1")
        self.assertEqual(mule.inventory_size, 140)

    def test_character_add_item(self):
        mule = Character().name("Mule1")
        soj = Item().name("The Stone Of Jordan").rolls(["+7 lightning damage"]).space(1)
        mule.add_item(soj)
        self.assertEqual(mule.inventory_size, 139)
        self.assertTrue(mule.has_item("The Stone Of Jordan"))

    def test_character_str(self):
        mule = Character().name("Mule1")
        soj = Item().name("The Stone Of Jordan").rolls(["+7 lightning damage"]).space(1)
        mule.add_item(soj)
        expected = "Mule1:\t1 items\t0 runes\t0 gems\t139 remaining inventory tiles"
        self.assertEqual(expected, str(mule))

    def test_gem(self):
        chipped_topaz = Gem().gem_type("Topaz").quality("chipped")
        chipped_topaz1 = Gem().gem_type("TOPAZ").quality("Chipped")
        self.assertEqual(chipped_topaz1,chipped_topaz)

    def test_character_inventory_list(self):
        mule = Character().name("Mule1")
        soj = Item().name("The Stone Of Jordan").rolls(["+7 lightning damage"]).space(1)
        mule.add_item(soj)
        for _ in range(5):
            mule.add_item(Rune().name("Ber"))
            mule.add_item(Gem().gem_type("Topaz").quality("Perfect"))
        print(mule.list_inventory_with_indices())



if __name__ == "__main__":
    unittest.main()

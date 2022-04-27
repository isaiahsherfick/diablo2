import unittest
from MuleManager import MuleManager
from Item import Item
from Rune import Rune


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
        soj3 = Item().name("The Stone Of Jordan").rolls(
            ["+9 lightning damage"])
        self.assertEqual(soj, soj2)
        self.assertNotEqual(soj, soj3)

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

    def TestRuneComparison(self):
        ist = Rune().name("Ist")
        jah = Rune().name("Jah")
        self.assertTrue(jah > ist)
        self.assertFalse(jah == ist)
        jah2 = Rune().name("JAH")
        self.assertEqual(jah, jah2)
        self.assertTrue(ist < jah2)



if __name__ == "__main__":
    unittest.main()

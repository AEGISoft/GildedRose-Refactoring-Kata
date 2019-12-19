# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_legendary_items_don_t_update(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)
        self.assertEquals(-1, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()

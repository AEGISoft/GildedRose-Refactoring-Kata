# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def update_quality(self, item_name, item_sell_in, expected_sell_in, item_quality, expected_quality):
        items = [Item(item_name, item_sell_in, item_quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(expected_sell_in, items[0].sell_in)
        self.assertEquals(expected_quality, items[0].quality)

    def test_legendary_items_don_t_update(self):
        self.update_quality("Sulfuras, Hand of Ragnaros",
                            item_sell_in=-1, expected_sell_in=-1,
                            item_quality=80, expected_quality=80)

    def test_normal_items_degrade_over_time(self):
        self.update_quality("brick",
                            item_sell_in=10, expected_sell_in=9,
                            item_quality=10, expected_quality=9)

    def test_normal_items_degrade_twice_as_fast_after_due_date(self):
        self.update_quality("brick",
                            item_sell_in=0, expected_sell_in=-1,
                            item_quality=10, expected_quality=8)

    def test_conjured_items_degrade_twice_as_fast_as_normal_items(self):
        self.update_quality("Conjured brick",
                            item_sell_in=10, expected_sell_in=9,
                            item_quality=10, expected_quality=8)
        self.update_quality("Conjured brick",
                            item_sell_in=0, expected_sell_in=-1,
                            item_quality=10, expected_quality=6)

    def test_quality_never_drops_below_zero(self):
        self.update_quality("brick",
                            item_sell_in=0, expected_sell_in=-1,
                            item_quality=0, expected_quality=0)

    def test_aged_brie_increases_in_quality_over_time(self):
        self.update_quality("Aged Brie",
                            item_sell_in=10, expected_sell_in=9,
                            item_quality=10, expected_quality=11)

    def test_even_aged_brie_doesnt_increases_in_quality_after_Fifty(self):
        self.update_quality("Aged Brie",
                            item_sell_in=10, expected_sell_in=9,
                            item_quality=50, expected_quality=50)

    def test_backstage_passes_increase_in_quality_over_time(self):
        self.update_quality("Backstage passes to a TAFKAL80ETC concert",
                            item_sell_in=20, expected_sell_in=19,
                            item_quality=10, expected_quality=11)

    def test_backstage_passes_increase_in_quality_twice_as_fast_if_ten_or_less_days_are_left(self):
        self.update_quality("Backstage passes to a TAFKAL80ETC concert",
                            item_sell_in=10, expected_sell_in=9,
                            item_quality=10, expected_quality=12)

    def test_backstage_passes_increase_in_quality_thrice_as_fast_if_five_or_less_days_are_left(self):
        self.update_quality("Backstage passes to a TAFKAL80ETC concert",
                            item_sell_in=5, expected_sell_in=4,
                            item_quality=10, expected_quality=13)

    def test_backstage_passes_drop_to_zero_quality_after_the_concert(self):
        self.update_quality("Backstage passes to a TAFKAL80ETC concert",
                            item_sell_in=0, expected_sell_in=-1,
                            item_quality=10, expected_quality=0)

    def test_backstage_passes_evolution(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEquals(11, items[0].sell_in)
        self.assertEquals(11, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(10, items[0].sell_in)
        self.assertEquals(12, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(14, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(8, items[0].sell_in)
        self.assertEquals(16, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(7, items[0].sell_in)
        self.assertEquals(18, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(6, items[0].sell_in)
        self.assertEquals(20, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(5, items[0].sell_in)
        self.assertEquals(22, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(25, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(3, items[0].sell_in)
        self.assertEquals(28, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(31, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(34, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(37, items[0].quality)

        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()

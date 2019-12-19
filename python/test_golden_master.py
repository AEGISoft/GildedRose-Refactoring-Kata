import unittest
from gilded_rose import Item, GildedRose


class GoldenMasterTest(unittest.TestCase):
    def test_golden_master(self):
        output_file = None
        try:
            output_file = open("output.txt", 'r')
            golden_master_lines = [output_file.readlines()]

        finally:
            output_file.close()

        lines = golden_master_test_run()

        for i in range(len(golden_master_lines) - 1):
            self.assertEquals(golden_master_lines[i], lines[i])


def golden_master_test_run():
    lines = ["OMGHAI!"]
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
    ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        lines.append("-------- day %s --------" % day)
        lines.append("name, sellIn, quality")
        for item in items:
            lines.append(str(item))
        lines.append("")
        GildedRose(items).update_quality()

    return lines


def persist_golden_master_testrun():
    output_file = open("output.txt", mode="w+")
    for line in golden_master_test_run():
        output_file.write(line)
        output_file.write("\n")


if __name__ == '__main__':
    unittest.main()

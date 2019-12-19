# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.updater = Item.get_updater_for(self)

    @staticmethod
    def get_updater_for(item):
        if item.is_of_legendary_type():
            return LegendaryItemUpdater(item)
        elif item.is_of_type_event():
            return EventItemUpdater(item)
        elif item.is_of_aging_beautifully_type():
            return BeautifullyAgingItemUpdater(item)
        elif item.is_of_conjured_type():
            return ConjuredItemUpdater(item)
        else:
            return StandardItemUpdater(item)

    def is_of_type_event(self):
        return self.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_of_legendary_type(self):
        return self.name == "Sulfuras, Hand of Ragnaros"

    def is_of_aging_beautifully_type(self):
        return self.name == "Aged Brie"

    def is_of_decreasing_quality_type(self):
        return not self.is_of_aging_beautifully_type() \
               and not self.is_of_type_event() \
               and not self.is_of_legendary_type()

    def is_of_conjured_type(self):
        return self.name == "conjured"

    def update(self):
        self.updater.update()

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class StandardItemUpdater:
    def __init__(self, item: Item):
        self.item = item

    def update(self):
        self._update_sell_in()
        self._update_quality()

    def _update_sell_in(self):
        self.item.sell_in -= 1

    def _update_quality(self):
        self.decrease_quality()

        if self.item.sell_in < 0:
            self.decrease_quality()

    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality += -1


class LegendaryItemUpdater(StandardItemUpdater):
    def __init__(self, item):
        super().__init__(item)

    def _update_sell_in(self):
        self.item.sell_in += 0

    def _update_quality(self):
        self.item.quality += 0


class EventItemUpdater(StandardItemUpdater):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality(self):
        self.increase_quality()

        if self.item.sell_in < 10:
            self.increase_quality()

        if self.item.sell_in < 5:
            self.increase_quality()

        if self.item.sell_in < 0:
            self.item.quality = 0


class BeautifullyAgingItemUpdater(StandardItemUpdater):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality(self):
        self.increase_quality()


class ConjuredItemUpdater(StandardItemUpdater):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality(self):
        self.decrease_quality()
        self.decrease_quality()

        if self.item.sell_in < 0:
            self.decrease_quality()
            self.decrease_quality()

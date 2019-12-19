# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = []
        for item in items:
            if item.is_of_legendary_type():
                self.items.append(Legendary(item))
            elif item.is_of_type_event():
                self.items.append(Event(item))
            elif item.is_of_aging_beautifully_type():
                self.items.append(BeautifullyAging(item))
            elif item.is_of_conjured_type():
                self.items.append(Conjured(item))
            else:
                self.items.append(Standard(item))

    def update_quality(self):
        for item in self.items:
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

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

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Standard:
    def __init__(self, item: Item):
        self.item = item

    def update(self):
        self._update_sell_in()
        self._update_quality()

    def _update_sell_in(self):
        self.item.sell_in -= 1

    def _update_quality(self):
        if self.item.quality > 0:
            self.item.quality += -1

        if self.item.quality > 0 and self.item.sell_in < 0:
            self.item.quality += -1


class Legendary(Standard):
    def __init__(self, item):
        super().__init__(item)

    def _update_sell_in(self):
        self.item.sell_in += 0

    def _update_quality(self):
        self.item.quality += 0


class Event(Standard):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality(self):
        self.item.quality += 1

        if self.item.sell_in < 10:
            self.item.quality += 1

        if self.item.sell_in < 5:
            self.item.quality += 1

        if self.item.sell_in < 0:
            self.item.quality = 0


class BeautifullyAging(Standard):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1


class Conjured(Standard):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality(self):
        if self.item.quality > 0:
            self.item.quality += -1
        if self.item.quality > 0:
            self.item.quality += -1

        if self.item.sell_in < 0:
            if self.item.quality > 0:
                self.item.quality += -1
            if self.item.quality > 0:
                self.item.quality += -1

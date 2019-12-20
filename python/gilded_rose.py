# -*- coding: utf-8 -*-


# represents all the items on sale in the Gilded Rose shop
class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


# represents an item for sale in the Gilded Rose shop
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.updater = ItemUpdater.create_for(self)

    def is_conjured(self):
        return self.name.startswith("Conjured")

    def is_event(self):
        return self.name.startswith("Backstage passes")

    def is_legendary(self):
        return self.name == "Sulfuras, Hand of Ragnaros"

    def is_aging_beautifully(self):
        return self.name == "Aged Brie"

    def update(self):
        self.updater.update()

    def is_passed_due_date(self):
        return self.sell_in < 0

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# template & factory for updating different kinds of Items
class ItemUpdater:
    def __init__(self, item):
        self.item = item
        self._max_quality = 50
        self._min_quality = 0

    # - factory --------------------------------------------------------------------
    @staticmethod
    def create_for(item):
        if item.is_legendary():
            return LegendaryUpdater(item)
        if item.is_event():
            return EventUpdater(item)
        if item.is_aging_beautifully():
            return AgingBeautifullyItemUpdater(item)
        if item.is_conjured():
            return ConjuredUpdater(item)
        return StandardUpdater(item)
    # - end factory -----------------------------------------------------------------

    # - template --------------------------------------------------------------------
    def update(self):
        self._reduce_sell_in()
        self._update_quality()
        if self.item.is_passed_due_date():
            self._past_due_date_adjustments()

    def _reduce_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def _update_quality(self):
        pass

    def _past_due_date_adjustments(self):
        pass
    # - end template ----------------------------------------------------------------

    # - protected parts -------------------------------------------------------------
    def _make_worthless(self):
        self.item.quality = self._min_quality

    def _decrease_quality(self):
        if self.item.quality > self._min_quality:
            self.item.quality = self.item.quality - 1

    def _increase_quality(self):
        if self.item.quality < self._max_quality:
            self.item.quality = self.item.quality + 1
    # - end protected parts ---------------------------------------------------------


# legendary items don't update !  they just exist :)
class LegendaryUpdater(ItemUpdater):
    def __init__(self, item):
        super().__init__(item)

    def _reduce_sell_in(self):
        pass


# events become more value-able when the due date approaches
# and worthless after the event has passed
class EventUpdater(ItemUpdater):
    def __init__(self, item):
        super().__init__(item)
        self._double_rate_sell_in = 10
        self._triple_rate_sell_in = 5

    def _update_quality(self):
        self._increase_quality()
        if self.item.sell_in < self._double_rate_sell_in:
            self._increase_quality()
        if self.item.sell_in < self._triple_rate_sell_in:
            self._increase_quality()

    def _past_due_date_adjustments(self):
        self._make_worthless()


# unlike standard items, this one gets better when time passes
class AgingBeautifullyItemUpdater(ItemUpdater):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality(self):
        self._increase_quality()


# degrades twice as fast as standard Items (note to marketing: get rid of these ASAP)
class ConjuredUpdater(ItemUpdater):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality(self):
        self._decrease_quality()
        self._decrease_quality()

    def _past_due_date_adjustments(self):
        self._decrease_quality()
        self._decrease_quality()


# default update behavior
class StandardUpdater(ItemUpdater):
    def __init__(self, item):
        super().__init__(item)

    def _update_quality(self):
        self._decrease_quality()

    def _past_due_date_adjustments(self):
        self._decrease_quality()

from enum import Enum

class ListType(Enum):
    DEBUG = 0
    ITEM = 1
    PARTY = 2
    CARD = 3
    MAP = 4

class ItemType(Enum):
    NONE = 0
    IMPORTANT = 1
    KEY = 2
    COOKINGDISK = 3
    VANILLA = 4
    RECIPE = 5

class CardType(Enum):
    NONE = 0
    GROUND = 1
    SHOP = 2

class RecipeType(Enum):
    NONE = 0
    USELESS = 1
    GROUND = 2
    SINGLE = 3
    DOUBLE = 4

class MysteryBox(Enum):
    NO = 0
    YES = 1

class TMapType(Enum):
    NONE = 0
    ITEM = 1
    CARD = 2

class ItemEntry:
    def __init__(self, name, hex, ListType, ItemType, CardType, RecipeType, MysteryBox, TMapType, BuyPrices, SellPrices):
        self.name = name
        self.hex = hex
        self.ListType = ListType
        self.ItemType = ItemType
        self.CardType = CardType
        self.RecipeType = RecipeType
        self.MysteryBox = MysteryBox
        self.TMapType = TMapType
        self.BuyPrices = BuyPrices
        self.SellPrices = SellPrices

class BuyPrice:
    def __init__(self, flip_buy, flop_buy, yold_buy, crag_buy, space_buy, flip_itty, flop_itty, dot_itty, crag_itty, over_itty, card_shop, map_shop):
        self.flip_buy = flip_buy
        self.flop_buy = flop_buy
        self.yold_buy = yold_buy
        self.crag_buy = crag_buy
        self.space_buy = space_buy
        self.flip_itty = flip_itty
        self.flop_itty = flop_itty
        self.dot_itty = dot_itty
        self.crag_itty = crag_itty
        self.over_itty = over_itty
        self.card_shop = card_shop
        self.map_shop = map_shop

class SellPrice:
    def __init__(self, home_sell, yold_sell, crag_sell, card_sell):
        self.home_sell = home_sell
        self.yold_sell = yold_sell
        self.crag_sell = crag_sell
        self.card_sell = card_sell

HexList = [
  ItemEntry (
      "NULL",
      0x0,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x1",
      0x1,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x2",
      0x2,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x3",
      0x3,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x4",
      0x4,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x5",
      0x5,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x6",
      0x6,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x7",
      0x7,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x8",
      0x8,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x9",
      0x9,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0xA",
      0xA,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0xC",
      0xB,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0xC",
      0xC,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0xD",
      0xD,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0xE",
      0xE,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0xF",
      0xF,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Ruins Key",
      0x10,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Door Key",
      0x11,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "House Key",
      0x12,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Fort Key",
      0x13,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Fort Key",
      0x14,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Fort Key",
      0x15,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Goldfish Bowl",
      0x16,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Goldfish Bowl", # Unused in game
      0x17,
      ListType.DEBUG,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Helmet",
      0x18,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Ancient Clue",
      0x19,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Door Key",
      0x1A,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Dimension Key",
      0x1B,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Dimension Key",
      0x1C,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Dimension Key",
      0x1D,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Water Tablet",
      0x1E,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Stone Tablet",
      0x1F,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Fire Tablet",
      0x20,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Cave Key",
      0x21,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Cave Key",
      0x22,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Card Key",
      0x23,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Floro Sprout",
      0x24,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Door Key",
      0x25,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Door Key",
      0x26,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Diet Book",
      0x27,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Door Key",
      0x28,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Blue Orb",
      0x29,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Yellow Orb",
      0x2A,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Red Orb",
      0x2B,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Pit Key",
      0x2C,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "undefined 0x2D",
      0x2D,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Castle Bleck Key",
      0x2E,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Old Key",
      0x2F,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Pit Key",
      0x30,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Door Key",
      0x31,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Return Pipe",
      0x32,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Crystal Ball",
      0x33,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Training Machine",
      0x34,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "You-Know-What",
      0x35,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Paper",
      0x36,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Autograph",
      0x37,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Random House Key",
      0x38,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Cooking Disk R",
      0x39,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Cooking Disk W",
      0x3A,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Cooking Disk Y",
      0x3B,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Cooking Disk B",
      0x3C,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Cooking Disk G",
      0x3D,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Cooking Disk PU",
      0x3E,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Cooking Disk PI", # Unused in game
      0x3F,
      ListType.DEBUG,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Golden Card",
      0x40,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None, None)
  ),
  ItemEntry (
      "Fire Burst",
      0x41,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(20, None, 7, 15, None, None, None, None, None, None, None, None),
      SellPrice(10, 4, 8, None)
  ),
  ItemEntry (
      "Ice Storm",
      0x42,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(40, None, None, 25, None, None, None, None, None, None, None, None),
      SellPrice(20, 30, 13, None)
  ),
  ItemEntry (
      "Thunder Rage",
      0x43,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 80, None, None, None, None, None, None, None, None, None, None),
      SellPrice(40, 100, 40, None)
  ),
  ItemEntry (
      "Shooting Star",
      0x44,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(80, 150, 80, None)
  ),
  ItemEntry (
      "POW Block",
      0x45,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, 60, 80, None, None, None, None, None, None, None, None,),
      SellPrice(80, 150, 80, None)
  ),
  ItemEntry (
      "Shell Shock",
      0x46,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(20, None, 8, None, None, None, None, None, None, None, None, None),
      SellPrice(10, 4, 10, None)
  ),
  ItemEntry (
      "Gold Bar",
      0x47,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(100, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(90, 120, 115, None)
  ),
  ItemEntry (
      "Gold Bar x3",
      0x48,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 300, None, None, None, None, None, None, None, None, None, None),
      SellPrice(300, 375, 350, None)
  ),
  ItemEntry (
      "Block Block",
      0x49,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 50, None, None, None, None, None, None, None, None, None, None),
      SellPrice(25, 25, 25, None)
  ),
  ItemEntry (
      "Courage Shell",
      0x4A,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(10, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(5, 13, 4, None)
  ),
  ItemEntry (
      "Mighty Tonic",
      0x4B,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 70, None, None, None, None, None, None, None, None, None, None),
      SellPrice(35, 25, 35, None)
  ),
  ItemEntry (
      "Volt Shroom",
      0x4C,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 30, None, None, None, None, None, None, None, None, None, None),
      SellPrice(15, 10, 15, None)
  ),
  ItemEntry (
      "Ghost Shroom",
      0x4D,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 88, None, None, None, None, None, None, None, None, None, None),
      SellPrice(44, 44, 44, None)
  ),
  ItemEntry (
      "Sleepy Sheep",
      0x4E,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(10, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(5, 13, 15, None)
  ),
  ItemEntry (
      "Stop Watch",
      0x4F,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 50, None, None, None, None, None, None, None, None, None, None),
      SellPrice(25, 25, 25, None)
  ),
  ItemEntry (
      "Shroom Shake",
      0x50,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(30, None, 11, 25, None, None, None, None, None, None, None, None),
      SellPrice(15, 11, 13, None)
  ),
  ItemEntry (
      "Super Shroom Shake",
      0x51,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 80, None, 100, None, None, None, None, None, None, None, None),
      SellPrice(40, 40, 50, None)
  ),
  ItemEntry (
      "Ultra Shroom Shake",
      0x52,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 300, None, None, None, None, None, None, None, None, None, None),
      SellPrice(150, 150, 150, None)
  ),
  ItemEntry (
      "Dried Shroom",
      0x53,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(1, 1, 1, None)
  ),
  ItemEntry (
      "Life Shroom",
      0x54,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(100, None, 50, 75, None, None, None, None, None, None, None, None),
      SellPrice(50, 25, 38, None)
  ),
  ItemEntry (
      "Long-Last Shake",
      0x55,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(30, None, 15, None, None, None, None, None, None, None, None, None),
      SellPrice(15, 8, 15, None)
  ),
  ItemEntry (
      "Mystery Box",
      0x56,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, 3, None, None, None, None, None, None, None, None),
      SellPrice(5, 5, 2, None)
  ),
  ItemEntry (
      "Catch Card",
      0x57,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, 10, None),
      SellPrice(10, 10, 10, None)
  ),
  ItemEntry (
      "Catch Card SP",
      0x58,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, 100, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "HP Plus",
      0x59,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(400, 400, 400, None)
  ),
  ItemEntry (
      "Power Plus",
      0x5A,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(400, 400, 400, None)
  ),
  ItemEntry (
      "Blue Apple",
      0x5B,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(15, 15, 15, None)
  ),
  ItemEntry (
      "Yellow Apple / Orange Apple",
      0x5C,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(15, 15, 15, None)
  ),
  ItemEntry (
      "Red Apple",
      0x5D,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(15, 15, 15, None)
  ),
  ItemEntry (
      "Pink Apple",
      0x5E,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(15, 15, 15, None)
  ),
  ItemEntry (
      "Black Apple",
      0x5F,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(1, 1, 1, None)
  ),
  ItemEntry (
      "Star Medal",
      0x60,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(50, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(25, 25, 25, None)
  ),
  ItemEntry (
      "Gold Medal",
      0x61,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.USELESS,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, 500, None, None, None, None, None, None, None, None, None, None),
      SellPrice(250, 250, 250, None)
  ),
  ItemEntry (
      "Poison Shroom",
      0x62,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(2, 2, 2, None)
  ),
  ItemEntry (
      "Slimy Shroom",
      0x63,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(40, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(20, 20, 20, None)
  ),
  ItemEntry (
      "Peachy Peach",
      0x64,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, 25, None, None, None, None),
      SellPrice(13, 13, 13, None)
  ),
  ItemEntry (
      "Keel Mango",
      0x65,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, 20, None, None, None),
      SellPrice(10, 10, 10, None)
  ),
  ItemEntry (
      "Primordial Fruit",
      0x66,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, 22, None, None, None, None, None, None, None, None),
      SellPrice(25, 25, 11, None)
  ),
  ItemEntry (
      "Golden Leaf",
      0x67,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(45, 45, 45, None)
  ),
  ItemEntry (
      "Turtley Leaf",
      0x68,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(5, 5, 5, None)
  ),
  ItemEntry (
      "Cake Mix",
      0x69,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, 25, None, None, None, None, None, None),
      SellPrice(13, 13, 13, None)
  ),
  ItemEntry (
      "Whacka Bump",
      0x6A,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(150, 150, 150, None)
  ),
  ItemEntry (
      "Horsetail",
      0x6B,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, 18, None, None, None, None),
      SellPrice(9, 9, 9, None)
  ),
  ItemEntry (
      "Fresh Pasta Bunch",
      0x6C,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, 30, None, None, None, None, None),
      SellPrice(15, 15, 15, None)
  ),
  ItemEntry (
      "Hot Sauce",
      0x6D,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, 20, None, None),
      SellPrice(10, 10, 10, None)
  ),
  ItemEntry (
      "Inky Sauce",
      0x6E,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(15, 15, 15, None)
  ),
  ItemEntry (
      "Dayzee Tear",
      0x6F,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(25, 25, 25, None)
  ),
  ItemEntry (
      "Sap Soup",
      0x70,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(8, 8, 8, None)
  ),
  ItemEntry (
      "Bone-In Cut",
      0x71,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(30, 30, 30, None)
  ),
  ItemEntry (
      "Fresh Veggie",
      0x72,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, 20, None, None, None, None),
      SellPrice(10, 10, 10, None)
  ),
  ItemEntry (
      "Smelly Herb",
      0x73,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, 15, None, None, None, None, None),
      SellPrice(8, 8, 8, None)
  ),
  ItemEntry (
      "Honey Jar",
      0x74,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, 20, None, None, None, None, None, None),
      SellPrice(10, 10, 10, None)
  ),
  ItemEntry (
      "Power Steak",
      0x75,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, 25, None, None, None, None, None, None),
      SellPrice(18, 18, 18, None)
  ),
  ItemEntry (
      "Big Egg",
      0x76,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, 35, None, None, None, None, None),
      SellPrice(13, 13, 13, None)
  ),
  ItemEntry (
      "Mild Cocoa Bean",
      0x77,
      ListType.ITEM,
      ItemType.VANILLA,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, 20, None, None, None),
      SellPrice(10, 10, 10, None)
  ),
  ItemEntry (
      "Sweet Choco-bar",
      0x78,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, 10, None, None, None, None, None, None, None),
      SellPrice(5, 5, 5, None)
  ),
  ItemEntry (
      "Shroom Choco-bar",
      0x79,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, 50, None, None, None, None, None, None, None),
      SellPrice(25, 25, 25, None)
  ),
  ItemEntry (
      "Golden Choco-bar",
      0x7A,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, 100, None, None, None, None, None, None, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "Gradual Syrup",
      0x7B,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "Dayzee Syrup",
      0x7C,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(35, 35, 35, None)
  ),
  ItemEntry (
      "Slimy Extract",
      0x7D,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(30, 30, 30, None)
  ),
  ItemEntry (
      "Fried Shroom Plate",
      0x7E,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(35, 35, 35, None)
  ),
  ItemEntry (
      "Roast Shroom Dish",
      0x7F,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(96, 96, 96, None)
  ),
  ItemEntry (
      "Shroom Steak",
      0x80,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(180, 180, 180, None)
  ),
  ItemEntry (
      "Honey Shroom",
      0x81,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(58, 58, 58, None)
  ),
  ItemEntry (
      "Honey Super",
      0x82,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(118, 118, 118, None)
  ),
  ItemEntry (
      "Shroom Broth",
      0x83,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(118, 118, 118, None)
  ),
  ItemEntry (
      "Mushroom Crepe",
      0x84,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(65, 65, 65, None)
  ),
  ItemEntry (
      "Shroom Cake",
      0x85,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(125, 125, 125, None)
  ),
  ItemEntry (
      "Chocolate Cake",
      0x86,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(55, 55, 55, None)
  ),
  ItemEntry (
      "Heartful Cake",
      0x87,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(75, 75, 75, None)
  ),
  ItemEntry (
      "Mousse",
      0x88,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(60, 60, 60, None)
  ),
  ItemEntry (
      "Peach Tart",
      0x89,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "Horsetail Tart",
      0x8A,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(60, 60, 60, None)
  ),
  ItemEntry (
      "Sweet Cookie Snack",
      0x8B,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(30, 30, 30, None)
  ),
  ItemEntry (
      "Koopa Dumpling",
      0x8C,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(40, 40, 40, None)
  ),
  ItemEntry (
      "Sap Muffin",
      0x8D,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(55, 55, 55, None)
  ),
  ItemEntry (
      "Town Special",
      0x8E,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(27, 27, 27, None)
  ),
  ItemEntry (
      "Mango Pudding",
      0x8F,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(55, 55, 55, None)
  ),
  ItemEntry (
      "Love Pudding",
      0x90,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(75, 75, 75, None)
  ),
  ItemEntry (
      "Couple's Cake",
      0x91,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(150, 150, 150, None)
  ),
  ItemEntry (
      "Fruit Parfait",
      0x92,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(70, 70, 70, None)
  ),
  ItemEntry (
      "Snow Cone",
      0x93,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(43, 43, 43, None)
  ),
  ItemEntry (
      "Snow Bunny",
      0x94,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(5, 5, 5, None)
  ),
  ItemEntry (
      "Berry Snow Bunny",
      0x95,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(5, 5, 5, None)
  ),
  ItemEntry (
      "Honey Candy",
      0x96,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(24, 24, 24, None)
  ),
  ItemEntry (
      "Electro Pop",
      0x97,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(82, 82, 82, None)
  ),
  ItemEntry (
      "Herb Tea",
      0x98,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(18, 18, 18, None)
  ),
  ItemEntry (
      "Koopa Tea",
      0x99,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(9, 9, 9, None)
  ),
  ItemEntry (
      "Spaghetti Plate",
      0x9A,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(35, 35, 35, None)
  ),
  ItemEntry (
      "Spicy Pasta Dish",
      0x9B,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(60, 60, 60, None)
  ),
  ItemEntry (
      "Ink Pasta Dish",
      0x9C,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(63, 63, 63, None)
  ),
  ItemEntry (
      "Koopasta Dish",
      0x9D,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(63, 63, 63, None)
  ),
  ItemEntry (
      "Love Noodle Dish",
      0x9E,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(80, 80, 80, None)
  ),
  ItemEntry (
      "Fried Egg",
      0x9F,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(30, 30, 30, None)
  ),
  ItemEntry (
      "Egg Bomb",
      0xA0,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "Dyllis Dynamite",
      0xA1,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(66, 66, 66, None)
  ),
  ItemEntry (
      "Spit Roast / Roast Meat",
      0xA2,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "Meteor Meal",
      0xA3,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(205, 205, 205, None)
  ),
  ItemEntry (
      "Omelette Plate",
      0xA4,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "Spicy Soup",
      0xA5,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(23, 23, 23, None)
  ),
  ItemEntry (
      "Hot Dog",
      0xA6,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, 120, None, None),
      SellPrice(60, 60, 60, None)
  ),
  ItemEntry (
      "Healthy Salad",
      0xA7,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(28, 28, 28, None)
  ),
  ItemEntry (
      "Dyllis Dinner",
      0xA8,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(100, 100, 100, None)
  ),
  ItemEntry (
      "Dyllis Special",
      0xA9,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(160, 160, 160, None)
  ),
  ItemEntry (
      "Dyllis Deluxe",
      0xAA,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(225, 225, 225, None)
  ),
  ItemEntry (
      "Space Food",
      0xAB,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(60, 60, 60, None)
  ),
  ItemEntry (
      "Emergency Ration",
      0xAC,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(40, 40, 40, None)
  ),
  ItemEntry (
      "Dangerous Delight",
      0xAD,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(3, 3, 3, None)
  ),
  ItemEntry (
      "Trial Stew",
      0xAE,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(2, 2, 2, None)
  ),
  ItemEntry (
      "Mistake",
      0xAF,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(1, 1, 1, None)
  ),
  ItemEntry (
      "Mistake (Sleepy Sheep)",
      0xB0,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(1, 1, 1, None)
  ),
  ItemEntry (
      "Warm Cocoa",
      0xB1,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(25, 25, 25, None)
  ),
  ItemEntry (
      "Odd Dinner",
      0xB2,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(33, 33, 33, None)
  ),
  ItemEntry (
      "Inky Soup",
      0xB3,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(20, 20, 20, None)
  ),
  ItemEntry (
      "Gingerbread House",
      0xB4,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(130, 130, 130, None)
  ),
  ItemEntry (
      "Volcano Shroom",
      0xB5,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(60, 60, 60, None)
  ),
  ItemEntry (
      "Koopa Pilaf",
      0xB6,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(45, 45, 45, None)
  ),
  ItemEntry (
      "Spicy Dinner",
      0xB7,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(40, 40, 40, None)
  ),
  ItemEntry (
      "Shroom Pudding",
      0xB8,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(65, 65, 65, None)
  ),
  ItemEntry (
      "Heavy Meal",
      0xB9,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(10, 10, 10, None)
  ),
  ItemEntry (
      "Primordial Dinner",
      0xBA,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(60, 60, 60, None)
  ),
  ItemEntry (
      "Gorgeous Steak",
      0xBB,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(75, 75, 75, None)
  ),
  ItemEntry (
      "Golden Meal",
      0xBC,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "Luxurious Set",
      0xBD,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "Roast Whacka Bump",
      0xBE,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(200, 200, 200, None)
  ),
  ItemEntry (
      "Dyllis Breakfast",
      0xBF,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(60, 60, 60, None)
  ),
  ItemEntry (
      "Dyllis Lunch",
      0xC0,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(75, 75, 75, None)
  ),
  ItemEntry (
      "Sky Juice",
      0xC1,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(20, 20, 20, None)
  ),
  ItemEntry (
      "Stamina Juice",
      0xC2,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(50, 50, 50, None)
  ),
  ItemEntry (
      "Choco Pasta Dish",
      0xC3,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(60, 60, 60, None)
  ),
  ItemEntry (
      "Shroom Delicacy",
      0xC4,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.DOUBLE,
      MysteryBox.NO,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(55, 55, 55, None)
  ),
  ItemEntry (
      "Roast Horsetail",
      0xC5,
      ListType.ITEM,
      ItemType.RECIPE,
      CardType.NONE,
      RecipeType.SINGLE,
      MysteryBox.YES,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None, None, None, None),
      SellPrice(25, 25, 25, None)
  ),
]

def searchList(name_or_id):
    try:
        input_as_int = int(name_or_id, 16)
    except ValueError:
        input_as_int = None

    matching_items = []
    for item in HexList:
        if item.name.lower() == name_or_id.lower() or (isinstance(item.hex, int) and item.hex == input_as_int):
            matching_items.append(item)

    return matching_items

with open ("bighexlist.py", "w") as f:
    f.write("ItemEntry = " + repr(HexList))

while True:
    searchInput = input("Enter the item name or hex value: ").lower()
    results = searchList(searchInput)

    if not results:
        print("Item not found")
    else:
        if len(results) == 1:
            result = results[0]
        else:
            print("Multiple items found:")
            for i, item in enumerate(results):
                print(f"{i + 1}: {item.name}, 0x{item.hex:03X}")
            choice = input("Enter the number of the item you want: ")
            try:
                choice = int(choice)
                if choice < 1 or choice > len(results):
                    print("Invalid choice")
                    continue
                result = results[choice - 1]
            except ValueError:
                print("Invalid choice")
                continue

        print(f"Name: {result.name}")
        print(f"Hex: 0x{result.hex:03X}")
        print(f"ListType: {result.ListType.name}")
        print(f"ItemType: {result.ItemType.name}")
        print(f"CardType: {result.CardType.name}")
        print(f"RecipeType: {result.RecipeType.name}")
        print(f"MysteryBox: {result.MysteryBox.name}")
        print(f"TMapType: {result.TMapType.name}")
        print(f"BuyPrices: Home: {result.BuyPrices.flip_buy}, Yold: {result.BuyPrices.yold_buy}, Crag: {result.BuyPrices.crag_buy}")
        print(f"SellPrices: Home: {result.SellPrices.home_sell}, Yold: {result.SellPrices.yold_sell}, Crag: {result.SellPrices.crag_sell}")

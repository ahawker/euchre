"""
    euchre/model
    ~~~~~~~~~~~~

    Contains types used to represent a card game of Euchre.
"""
import enum
import itertools
import random


class Color(enum.IntEnum):
    """
    Defines one of the two available card suit colors.
    """

    BLACK = 1
    RED = 2


class Suit(enum.IntEnum):
    """
    Defines the four available card suits.
    """

    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    @property
    def color(self):
        """
        The suit color.

        :return: The color of the suit.
        :rtype: :class:`~euchre.model.Color`
        """
        return Color.BLACK if self % 4 <= 1 else Color.RED


#: All card ranks as a single string.
RANKS_STR = '9TJQKA'


#: Maps a single character string to its integer rank, e.g. "J" -> 11.
RANKS = dict(zip(RANKS_STR, range(9, 15)))


#: All card suits as a single string.
SUITS_STR = 'CDHS'


#: Maps a single character string to its :class:`~euchre.model.Suit` value, e.g. "D" -> Suit.DIAMONDS.
SUITS = dict(zip(SUITS_STR, Suit))


class Card:
    """
    Represents an individual playing card.
    """

    @classmethod
    def from_pair(cls, card):
        """
        Create a new instance from the given two item iterable.

        This can be a two character string, e.g. "AH" or a two item iterable, e.g. ("A", "H").

        :param card: Iterable used to create new instance.
        :type card: :class:`~str`, :class:`~tuple`, :class:`~list`
        :return: A new card instance created from the iterable.
        :rtype: :class:`~euchre.model.Card`
        :raises ValueError: When the iterable is not exactly 2 items long
        """
        if len(card) != 2:
            raise ValueError('Expects card to be two items; got {}'.format(len(card)))
        return cls(*card)

    def __init__(self, rank, suit):
        self._rank = RANKS[rank]
        self._suit = SUITS[suit]
        self._str = '{}{}'.format(rank, suit)

    def __repr__(self):
        return '<{}({})>'.format(self.__class__.__name__, str(self))

    def __str__(self):
        return self._str

    @property
    def rank(self):
        """
        The card numeric rank.

        :return: The numeric value of the card.
        :rtype: :class:`~int`
        """
        return self._rank

    @property
    def suit(self):
        """
        The card suit.

        :return: The suit of the card.
        :rtype: :class:`~euchre.model.Suit`
        """
        return self._suit


#: List of :class:`~euchre.model.Card` instances that represent all cards in a Euchre deck.
DECK_CARDS = [Card.from_pair(card) for card in itertools.product(RANKS_STR, SUITS_STR)]


class Deck:
    """
    Represents an individual deck of playing cards.
    """

    @classmethod
    def new(cls):
        """
        Create a new instance containing a fresh deck of cards that has been shuffled.

        :return: A new deck instance with shuffled cards.
        :rtype: :class:`~euchre.model.Deck`
        """
        cards = DECK_CARDS.copy()
        random.shuffle(cards)
        return cls(cards)

    def __init__(self, cards):
        self._cards = cards

    def __repr__(self):
        return '<{}({})>'.format(self.__class__.__name__, str(self))

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

    @property
    def cards(self):
        """
        Collection of :class:`~euchre.model.Card` in the deck.

        :return: A collection of all cards in the deck.
        :rtype: :class:`~list` of :class:`~euchre.model.Card`
        """
        return self._cards


class Hand:
    """
    Represents a collection of cards held by a single player.
    """

    @classmethod
    def from_str(cls, cards):
        cards = [Card.from_pair(card) for card in cards]
        return cls(cards)

    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return '<{}({})>'.format(self.__class__.__name__, str(self))

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


class Player:
    """
    Represents an individual participating in a game.
    """

    def __init__(self, hand):
        self._hand = hand

    @property
    def hand(self):
        return self._hand

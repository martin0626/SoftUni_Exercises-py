from project.card.card import Card
from project.card.trap_card import TrapCard
from project.card.magic_card import MagicCard


class CardRepository:

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        card_names = [c for c in self.cards if c.name == card.name]
        if card_names:
            raise ValueError(f'Card {card.name} already exists!')
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError('Card cannot be an empty string!')
        card_object = [c for c in self.cards if c.name == card][0]
        self.cards.remove(card_object)
        self.count += 1

    def find(self, name):
        card = [c for c in self.cards if name == c.name]
        if card:
            return card[0]

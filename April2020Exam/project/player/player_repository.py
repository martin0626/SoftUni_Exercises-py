from project.player.player import Player
from project.player.beginner import Beginner
from project.player.advanced import Advanced


class PlayerRepository:

    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        players_names = [p.username for p in self.players]
        if player.username in players_names:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        player_object = [p for p in self.players if p.username == player]
        self.players.remove(player_object[0])
        self.count -= 1

    def find(self, username):
        player = [p for p in self.players if username == p.username]
        if player:
            return player[0]

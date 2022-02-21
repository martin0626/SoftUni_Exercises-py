from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.trap_card import TrapCard
from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository
from project.player.player_repository import PlayerRepository


class BattleField:

    def fight(self, attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__name__ == 'Beginner':
            attacker.health += 40
            for c in attacker.card_repository.cards:
                c.damage_points += 30

        if enemy.__name__ == 'Beginner':
            enemy.health += 40
            for c in enemy.card_repository.cards:
                c.damage_points += 30

        attacker.health += sum([c.health_points for c in attacker.card_repository.cards])
        enemy.health += sum([c.health_points for c in enemy.card_repository.cards])

        for c in attacker.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            attacker.take_damage(c.damage_points)

        for c in enemy.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            enemy.take_damage(c.damage_points)



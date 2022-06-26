import random


class Player:
    def __init__(self, name: str, health: float, energy: float, strn: float):
        self.name = name
        self.health = health
        self.energy = energy
        self.strn = strn

    def show_stats(self):
        print(self.name)
        print('hp', self.health)
        print('energy', self.energy)
        print('str', self.strn)
    
    def hit_stats(self):
        hit_chance = random.random()
        hit_point = hit_chance * self.strn
        energy_lose = hit_chance * 10
        
        return hit_point, energy_lose
    
    def hit_enemy(self, enemy):
        hit_point_enemy, energy_lose_self = self.hit_stats()
        enemy.health -= hit_point_enemy
        self.energy -= energy_lose_self

        self.show_stats
    
    @staticmethod
    def is_dead(player):
        if player.health <= 0:
            return True

class Warrior(Player):
    def __init__(self, name: str, health: float, energy: float, strn: float):
        super().__init__(name, health, energy, strn)
    pass
class Mage(Player):
    def __init__(self, name: str, health: float, energy: float, strn: float):
        pass
class Healer(Player):
    def __init__(self, name: str, health: float, energy: float, strn: float):
        super().__init__(name, health, energy, strn)
        self.heal_point = 50
        
w = Warrior('Begüm', 100, 100, 10)
w.show_stats()
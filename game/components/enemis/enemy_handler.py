from game.components.enemis.ship import Ship
from game.components.enemis.enemy_2 import Enemy2

class EnemyHandler:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_visible:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 3:
            self.enemies.append(Ship())
            return 
        if len(self.enemies) < 4:
            self.enemies.append(Enemy2())
            return 
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
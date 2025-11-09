import math
import pygame

# Simple object class with minimal methods
class GameObject:
    def __init__(self, x, y, w, h, color, uses_gravity=True):
        self.x_position = x
        self.y_position = y
        self.width_value = w
        self.height_value = h
        self.color_value = color
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = 1
        self.uses_gravity = uses_gravity
        self.patrol_min = None
        self.patrol_max = None
        self.base_y = y if not uses_gravity else None
        self.phase_offset = 0
        self.speed_base = 0
        
    def get_rect_bounds(self):
        return pygame.Rect(self.x_position, self.y_position, self.width_value, self.height_value)
    
    def update_position(self):
        self.x_position += self.velocity_x * self.direction
        if self.uses_gravity:
            self.velocity_y += 0.8
            self.y_position += self.velocity_y
        
    def reverse_direction(self):
        self.direction *= -1

# Data-driven approach - just lists of objects
PlatformObjectClass = GameObject
EnemyObjectClass = GameObject

class PlatformManagerClass:
    def __init__(self):
        self.platform_list = [
            GameObject(0, 550, 800, 50, (34, 139, 34)),
            GameObject(200, 450, 150, 20, (139, 69, 19)),
            GameObject(400, 350, 150, 20, (139, 69, 19)),
            GameObject(600, 450, 150, 20, (139, 69, 19)),
            GameObject(300, 250, 150, 20, (139, 69, 19)),
            GameObject(500, 200, 150, 20, (139, 69, 19)),
            GameObject(100, 300, 100, 20, (139, 69, 19))
        ]
        
    def get_all_platforms(self):
        return self.platform_list

class EnemyManagerClass:
    def __init__(self):
        self.enemy_list = [
            GameObject(250, 410, 30, 30, (255, 165, 0), uses_gravity=False),
            GameObject(450, 310, 30, 30, (255, 165, 0), uses_gravity=False),
            GameObject(650, 410, 30, 30, (255, 165, 0), uses_gravity=False),
            GameObject(350, 210, 30, 30, (255, 165, 0), uses_gravity=False)
        ]
        for idx, enemy in enumerate(self.enemy_list):
            enemy.velocity_x = 2
            enemy.speed_base = 2
            enemy.patrol_min = enemy.x_position - 60
            enemy.patrol_max = enemy.x_position + 60
            enemy.base_y = enemy.y_position
            enemy.phase_offset = idx * 350
        
    def get_all_enemies(self):
        return self.enemy_list
        
    def update_all_enemies(self):
        current_time = pygame.time.get_ticks()
        for enemy in self.enemy_list:
            enemy.velocity_x = enemy.speed_base * (1 + 0.3 * math.sin((current_time + enemy.phase_offset) * 0.002))
            enemy.update_position()
            if enemy.patrol_min is not None and enemy.patrol_max is not None:
                if enemy.x_position <= enemy.patrol_min or enemy.x_position + enemy.width_value >= enemy.patrol_max:
                    enemy.x_position = max(enemy.patrol_min, min(enemy.x_position, enemy.patrol_max - enemy.width_value))
                    enemy.reverse_direction()
            if enemy.patrol_min is not None and enemy.base_y is not None:
                bob_amount = math.sin((current_time + enemy.phase_offset) * 0.004) * 18
                enemy.y_position = enemy.base_y + bob_amount
            
    def remove_enemy(self, enemy):
        if enemy in self.enemy_list:
            self.enemy_list.remove(enemy)

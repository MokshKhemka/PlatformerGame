import pygame

class GameObject:
    def __init__(self, x, y, w, h, color):
        self.x_position = x
        self.y_position = y
        self.width_value = w
        self.height_value = h
        self.color_value = color
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = 1
        
    def get_rect_bounds(self):
        return pygame.Rect(self.x_position, self.y_position, self.width_value, self.height_value)
    
    def update_position(self):
        self.x_position += self.velocity_x * self.direction
        self.velocity_y += 0.8
        self.y_position += self.velocity_y
        
    def reverse_direction(self):
        self.direction *= -1

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
            GameObject(250, 410, 30, 30, (255, 165, 0)),
            GameObject(450, 310, 30, 30, (255, 165, 0)),
            GameObject(650, 410, 30, 30, (255, 165, 0)),
            GameObject(350, 210, 30, 30, (255, 165, 0))
        ]
        for e in self.enemy_list:
            e.velocity_x = 2
        
    def get_all_enemies(self):
        return self.enemy_list
        
    def update_all_enemies(self):
        for enemy in self.enemy_list:
            enemy.update_position()
            
    def remove_enemy(self, enemy):
        if enemy in self.enemy_list:
            self.enemy_list.remove(enemy)


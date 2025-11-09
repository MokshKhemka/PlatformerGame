import pygame

class PlayerCharacterClass:
    def __init__(self, start_x, start_y):
        self.x_position = start_x
        self.y_position = start_y
        self.width_value = 40
        self.height_value = 40
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed_value = 5
        self.jump_power = -15
        self.gravity_force = 0.8
        self.on_ground_flag = False
        self.color_value = (255, 0, 0)
        self.start_x_position = start_x
        self.start_y_position = start_y
        self.max_jumps = 2
        self.jumps_remaining = 2
        self.jump_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        
    def handle_movement_input(self, keys_pressed):
        left = keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]
        right = keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]
        
        if left and not self.left_pressed:
            self.velocity_x = -self.speed_value
        if right and not self.right_pressed:
            self.velocity_x = self.speed_value
            
        self.left_pressed = left
        self.right_pressed = right
        
        jump_key = keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_UP]
        if jump_key and not self.jump_pressed and self.jumps_remaining > 0:
            self.velocity_y = self.jump_power
            self.jumps_remaining -= 1
            self.on_ground_flag = False
        self.jump_pressed = jump_key
            
    def apply_gravity_force(self):
        self.velocity_y += self.gravity_force
        
    def update_position(self):
        self.x_position += self.velocity_x
        self.y_position += self.velocity_y
        self.on_ground_flag = False
        if self.y_position > 600:
            self.y_position = 600
            self.velocity_y = 0
            self.on_ground_flag = True
            self.jumps_remaining = self.max_jumps
            
    def get_rect_bounds(self):
        return pygame.Rect(self.x_position, self.y_position, self.width_value, self.height_value)
        
    def bounce_off_enemy(self):
        self.velocity_y = -10
        
    def reset_position(self):
        self.x_position = self.start_x_position
        self.y_position = self.start_y_position
        self.velocity_x = 0
        self.velocity_y = 0
        self.jumps_remaining = self.max_jumps
        self.left_pressed = False
        self.right_pressed = False
        
    def set_on_ground(self, value):
        self.on_ground_flag = value
        if value:
            self.jumps_remaining = self.max_jumps
        
    def set_velocity_y(self, value):
        self.velocity_y = value
        
    def get_width(self):
        return self.width_value
        
    def get_height(self):
        return self.height_value


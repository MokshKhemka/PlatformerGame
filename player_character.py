import pygame

class PlayerCharacterClass:
    def __init__(self, start_x, start_y):
        self.x_position = start_x
        self.y_position = start_y
        self.width_value = 40
        self.height_value = 40
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0.6
        self.max_speed = 6
        self.friction = 0.0001
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
        self.dash_cooldown = 800
        self.dash_speed = 12
        self.dash_duration = 180
        self.dash_timer = 0
        self.last_dash_time = -self.dash_cooldown
        self.facing_direction = 1
        self.double_tap_window = 250
        self.last_left_tap_time = -self.double_tap_window
        self.last_right_tap_time = -self.double_tap_window
        self.drop_cooldown = 450
        self.drop_active = False
        self.drop_ready = False
        self.last_drop_time = -self.drop_cooldown
        
    def handle_movement_input(self, keys_pressed):
        left = keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]
        right = keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]
        down = keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]
        current_time = pygame.time.get_ticks()
        prev_left = self.left_pressed
        prev_right = self.right_pressed
        
        if left:
            self.velocity_x -= self.acceleration
            self.facing_direction = -1
        if right:
            self.velocity_x += self.acceleration
            self.facing_direction = 1
        if not left and not right and self.dash_timer <= 0:
            self.velocity_x *= self.friction
            if abs(self.velocity_x) < 0.05:
                self.velocity_x = 0
        self.velocity_x = max(-self.max_speed, min(self.velocity_x, self.max_speed))
        
        if left and not prev_left:
            if current_time - self.last_left_tap_time <= self.double_tap_window:
                self.start_dash(-1, current_time)
            self.last_left_tap_time = current_time
        if right and not prev_right:
            if current_time - self.last_right_tap_time <= self.double_tap_window:
                self.start_dash(1, current_time)
            self.last_right_tap_time = current_time
        if down and not self.on_ground_flag and not self.drop_active:
            if current_time - self.last_drop_time >= self.drop_cooldown:
                self.start_drop(current_time)
            
        self.left_pressed = left
        self.right_pressed = right
        
        jump_key = keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_UP]
        if jump_key and not self.jump_pressed and self.jumps_remaining > 0:
            self.velocity_y = self.jump_power
            self.jumps_remaining -= 1
            self.on_ground_flag = False
        self.jump_pressed = jump_key
        
    def start_dash(self, direction, current_time):
        if current_time - self.last_dash_time >= self.dash_cooldown and self.dash_timer <= 0:
            self.dash_timer = self.dash_duration
            self.last_dash_time = current_time
            self.facing_direction = direction
            self.color_value = (255, 140, 0)
            self.drop_active = False
            self.drop_ready = False
        
    def start_drop(self, current_time):
        self.drop_active = True
        self.drop_ready = False
        self.last_drop_time = current_time
        self.velocity_y = max(self.velocity_y, 22)
        self.color_value = (138, 43, 226)
        self.dash_timer = 0
        
    def update_dash_state(self):
        if self.dash_timer > 0:
            self.dash_timer -= 16
            if self.dash_timer < 0:
                self.dash_timer = 0
            self.velocity_x = self.dash_speed * self.facing_direction
            self.velocity_y = 0
        else:
            self.color_value = (255, 0, 0)
            
    def apply_gravity_force(self):
        if self.dash_timer > 0:
            return
        if self.drop_active:
            self.velocity_y += self.gravity_force * 1.6
        else:
            self.velocity_y += self.gravity_force
        
    def update_position(self):
        self.update_dash_state()
        self.x_position += self.velocity_x
        self.y_position += self.velocity_y
        self.on_ground_flag = False
        if self.y_position > 600:
            self.y_position = 600
            self.velocity_y = 0
            self.on_ground_flag = True
            self.jumps_remaining = self.max_jumps
            if self.drop_active:
                self.drop_ready = True
                self.drop_active = False
            self.color_value = (255, 0, 0)
            
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
        self.dash_timer = 0
        self.last_dash_time = -self.dash_cooldown
        self.last_left_tap_time = -self.double_tap_window
        self.last_right_tap_time = -self.double_tap_window
        self.drop_active = False
        self.drop_ready = False
        self.last_drop_time = -self.drop_cooldown
        self.color_value = (255, 0, 0)
        
    def set_on_ground(self, value):
        self.on_ground_flag = value
        if value:
            self.jumps_remaining = self.max_jumps
            if self.drop_active:
                self.drop_ready = True
                self.drop_active = False
            self.color_value = (255, 0, 0)
        
    def set_velocity_y(self, value):
        self.velocity_y = value
        
    def get_width(self):
        return self.width_value
        
    def get_height(self):
        return self.height_value
    
    def use_drop_pop(self):
        if self.drop_ready:
            self.drop_ready = False
            return True
        return False

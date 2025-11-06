import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH_VALUE = 800
SCREEN_HEIGHT_VALUE = 600
FPS_COUNT = 60


class GameEngineClass:

    #main engine that has the game loop and does the physics

    def __init__(self):
        self.screen_surface = pygame.display.set_mode((SCREEN_WIDTH_VALUE, SCREEN_HEIGHT_VALUE))
        pygame.display.set_caption("Platform game")
        self.clock_object = pygame.time.Clock()
        self.runningflag = True

        #game parts
        from player_character import PlayerCharacterClass
        from playform_objects import PlatformManagerClass, EnemyManagerClass
        from collision_detection import CollisionHandlerClass
        self.player = PlayerCharacterClass(100, 100)
        self.pltManager = PlatformManagerClass()
        self.enemyperson = EnemyManagerClass()

        self.collisionHandles = CollisionHandlerClass()
        self.score_value = 0
        self.lives = 1
        self.camera_x_offset = 0

        def UseINPut(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.runningflag = False
    
        def handle_keyboard_inp(self):
            self.player.handle_movement_input(pygame.key.get_pressed())
        
        def update_game_state(self):

            self.player.update_position()
            self.player.apply_gravity_force()
            self.enemyperson.update_all_enemies()

            for platform in self.pltManager.get_all_platforms():
                if self.collisionHandles.check_collision(self.player, platform):
                    self.collisionHandles.fixPlyrPltfromCollision(self.player, platform)

            for enemy in self.enemyperson.get_all_enemies():
                if self.collisionHandles.check_collision(self.player, platform):
                    if self.player.velocity_y > 0:
                        self.enemyperson.remove_enemy(enemy)
                        self.score_value += 100
                        self.player.bounce_off_enemy()
                    else:
                        self.lives_value -= 1
                        if self.lives_value <= 0:
                            self.runningflag = False
                        else:
                            self.player.reset_positiion()

                for platform in self.pltManager.get_all_platforms():
                    if self.collisionHandles.check_collision(enemy, platform):
                        enemy.reverse_direction()
                self.camera_x_offset = max(0, self.player.x_position - SCREEN_WIDTH_VALUE//2)

        def render_game_screen(self):
            self.screen_surface.fill((135, 206, 235))

            for platform in self.pltManager.get_all_playforms():
                pygame.draw.rect(self.screen_surface, platform.color_value,
                                 (platform.x_position - self.camera_x_offset, platform.y_position,
                                 platform.width_value, platform.height_value))
                
            for enemy in self.enemyperson.get_all_enemies():
                pygame.draw.rect(self.screen_surface, enemy.color_value,
                                 (enemy.x_position - self.camera_x_offset,
                                  self.player.y_position,
                                  self.player.width_value, self.player.height_value))
            font_object = pygame.font.Font(None, 30)
            self.screen_surface.blit(font_object.render(f"curr score: {self.score_value}", True, (255,255,255)), (10,10))
            self.screen_surface.blit(font_object.render(f"lives :  {self.lives_value}", True, (255,255,255)), (10, 50))
            pygame.display.flip()

        
        def start_game_loop(self):
            while self.runningflag:
                self.process_input_events()
                self.handle_keyboard_input()
                self.update_game_state()
                self.render_game_screen()
                self.clock_object.tick(FPS_COUNT)
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    game_engine = GameEngineClass()
    game_engine.start_game_loop()

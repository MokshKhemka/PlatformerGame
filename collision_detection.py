



import pygame

class CollisionHandlerClass:
    #basically checks if two objects are colliding and uses the second method to fix it
    def check_collision(self, obj1, obj2):
        firstRect = obj1.get_rect_bounds() if hasattr(obj1, 'get_rect_bounds') else None
        seconndRect = obj2.get_rect_bounds() if hasattr(obj2, 'get_rect_bounds') else None
        if not firstRect or not seconndRect:
            return False
        return firstRect.colliderect(seconndRect)

    def fixPlyrPltfromCollision(self, player, platform):
        player_rect = player.get_rect_bounds()
        platform_rect = platform.get_rect_bounds()

        left_ovrlap = player_rect.right - platform_rect.left
        right_overlap = platform_rect.right - player_rect.left
        overlapTop = player_rect.bottom - platform_rect.top
        overlapBottom = platform_rect.bottom - player_rect.top

        minOvr = min(left_ovrlap, right_overlap, overlapTop, overlapBottom)

        if minOvr == overlapTop:
            player.y_position = platform_rect.top - player.get_height()
            player.set_velocity_y(0)
            player.set_on_ground(True)

        elif minOvr == overlapBottom:
            player.y_position = platform_rect.bottom
            player.set_velocity_y(0)


        elif minOvr == left_ovrlap:
            player.x_position = platform_rect.left - player.get_width()
            player.velocity_x = 0

        elif minOvr == right_overlap:
            player.x_position = platform_rect.right
            player.velocity_x = 0


from pygame import *

class GameSprite(sprite, Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
    super().__init__()
    self.image = transform.scale(image.load(player_image))
    self.speed = player_speed
    self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y

class Player(GameSprite):
  def update(self):
    keys = Key.get_pressed()
    #if keys = [K_LEFT] and self.rect.x

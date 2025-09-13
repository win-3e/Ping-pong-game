from pygame import *

class GameSprite(sprite, Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
    super().__init__()
    self.image = transform.scale(image.load(player_image))
    self.speed = player_speed
    self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y
  def reset(self):
    window.blit(self.image (self.rect.x, self.rect.y))

class Player(GameSprite):
  def update_l(self):
    keys = Key.get_pressed()
    if keys = [K_w] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys = [K_s] and self.rect.y < (500-65):
      self.rect.y += self.speed
  def update_r(self):
    keys = Key.get_pressed()
    if keys = [K_UP] and self.rect.y >5:
      self.rect.y -= self.speed
    if keys = [K_DOWN] and self.rect.y < (500-65):
      self.rect.y += self.speed
    
    



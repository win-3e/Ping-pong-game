# Ping-pong-game 

from pygame import *

background= (200,255,255) 
window = display.set_mode((600,500))
window.fill(background)

clock = time.Clock()
FPS = 60run = True

while run: 
  for e in event.get():
    if e.type == QUIT:
      run = False

  display.update()
  clock.tick(FPS)

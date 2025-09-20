# Ping-pong-game 

from pygame import *
from ping_pong_classes import GameSprite, Player

window = display.set_mode((600,500))
background = transform.scale(image.load('ping_table.png'),(600,500))

clock = time.Clock()
ball = GameSprite('tennis_ball.png', p_x = 50 ,p_y =50, p_width = 60, p_height = 60, p_speed= 3)
racket1 = Player('racket.png', p_x=5, p_y=240, p_width=30, p_height=150, p_speed = 4)
racket2 = Player('racket.png', p_x=560, p_y=240, p_width=30, p_height=150, p_speed=4)

font.init()
font1 = font.SysFont('Arial', 35)
player1_lose = font1.render('PLAYER 1 LOST', True, (255,255,255))
font2 = font.SysFont('Arial', 35)
player2_lose = font2.render('PLAYER 2 LOST', True, (255,255,0))
style = font.SysFont('Arial', 25)


speed_x = 3
speed_y = 3

p1_score = 0
p2_score = 0

players = sprite.Group(racket1, racket2)
run = True
finish = True

while run: 
  for e in event.get():
    if e.type == QUIT:
      run = False
    
  if finish:
    window.blit(background, (0,0))
    ball.reset(window)

    text_p1_score = style.render("Player 1:"+ str(p1_score),1, (255,255,255))
    window.blit(text_p1_score, (12,7))

    text_p2_score = style.render("Player 2:" + str(p2_score), 1, (255,255, 0))
    window.blit(text_p2_score, (493,7))


    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y >= 440 or ball.rect.y <=0 :
      speed_y *= -1
    
    if sprite.spritecollide(ball, players, False):
      if sprite.collide_rect(racket2, ball):
        p2_score += 1
      if sprite.collide_rect(racket1, ball):
        p1_score += 1
      speed_x *= -1

    if ball.rect.x <= 0:
      window.blit(player1_lose, (200,200))
      finish = False
    
    if ball.rect.x >= 600:
      window.blit(player2_lose, (200,200))
      finish = False

    racket1.reset(window)
    racket2.reset(window)

    racket1.update_1()
    racket2.update_2()

  display.update()
  clock.tick(60)

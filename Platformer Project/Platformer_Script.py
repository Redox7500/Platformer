import pygame, sys
from pygame.locals import QUIT

pygame.init()

screen_w = 300
screen_h = 400
clock = pygame.time.Clock()
fps = 200
gravity = 0.4

screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption('Hello World!')
WHITE = (255, 255, 255)
player_img = pygame.image.load("diamond.png").convert_alpha()
bg_img = pygame.image.load("blue.jpeg").convert_alpha()
pygame.transform.scale(bg_img, (300, 400))
#platform_img = pygame.image.load("").convert_alpha()
#player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT -150)
pygame.transform.scale(bg_img, (screen_w, screen_h))
pygame.display.set_caption("Doodle Jump")


class Player():
  def __init__(self, x, y):
    self.image = pygame.transform.scale(player_img, (50, 42))
    self.width = 30
    self.height = 37
    self.rect = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = (x, y)
    self.vel_y = 0
    self.flip = False
  def draw(self):
    screen.blit(self.image, (self.rect.x - 11, self.rect.y - 4))
    pygame.draw.rect(screen, WHITE, self.rect, 2)
  def move(self):
    dx = 0
    dy = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
      dx = -5
      self.flip = True
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
      dx = 5
      self.flip = False
    self.vel_y += gravity
    dy += self.vel_y
    if dx + self.rect.left < 0:
      dx = -self.rect.left
    if dx + self.rect.right > screen_w:
      dx = screen_w - self.rect.right
    if self.rect.bottom + dy > screen_h:
      dy = 0
      self.vel_y = -10
    self.rect.x += dx
    self.rect.y += dy
player = Player(screen_w // 2, screen_h - 150)
    
run = True
while run: #event handler
  clock.tick(fps)
  screen.blit(bg_img, (0, 0))
  player.draw()
  player.move()
  
  for event in pygame.event.get():
    if event.type == QUIT:
      run = False
      pygame.quit()
      sys.exit()
    pygame.display.update()

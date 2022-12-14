# import library
import pygame 
from pygame.locals import *
import constants

#classes of the game
class Game():
    def __init__ (self):
      pygame.init()
      self.window = pygame.display.set_mode(constants.size)
      self.title = pygame.display.set_caption(constants.title)
      self.window.fill(constants.bg_color)
      self.icon = pygame.image.load("images\culebrita.png")
      pygame.display.set_icon(self.icon)
      pygame.display.update()

    def run(self):
      #Creating a bool value which checks
      #if game is running
      running = True

      #Keep game running till running is true
      while running:
        for event in pygame.event.get():
          if event.type == KEYDOWN :
             if event.key == K_ESCAPE:
                running = False
          elif event.type ==  QUIT:
              running = False 


game = Game()
game.run()
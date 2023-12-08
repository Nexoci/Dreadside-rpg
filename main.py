#Made by: Konnor and Jack
#Made on: 2023/12/05
#A viking meets ww2 rpg

import pygame,sys


pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

#Setup of Starting objects

window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("DREADSIDE")
def display():
    window.fill((255,255,255))
   
   

while True:
    display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw
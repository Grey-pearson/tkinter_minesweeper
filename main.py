import pygame, sys
from random import randrange
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()
bomb = pygame.image.load("imgs/bomb.png")
pygame.display.set_icon(bomb)
surfObj = pygame.display.set_mode((173, 200))
pygame.display.set_caption("Minesweeper")




class Block:
    def __init__(self, type) -> None:
        self.type = type
        self.img = 

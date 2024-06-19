import pygame
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

font = pygame.font.Font("imgs/UniversLTStd-BoldEx.otf", 18)

bomb = pygame.image.load("imgs/bomb.png")

blockSurf = pygame.image.load("imgs/block.png")
blockSurfSel = pygame.image.load("imgs/selblock.png")
blockSurfBlank = pygame.image.load("imgs/blankblock.png")

warn1 = pygame.image.load("imgs/block1.png")
warn2 = pygame.image.load("imgs/block2.png")
warn3 = pygame.image.load("imgs/block3.png")
warn4 = pygame.image.load("imgs/block4.png")
warn5 = pygame.image.load("imgs/block5.png")
warn6 = pygame.image.load("imgs/block6.png")
warn7 = pygame.image.load("imgs/block7.png")
warn8 = pygame.image.load("imgs/block8.png")
explode = pygame.image.load("imgs/explode.png")
flag = pygame.image.load("imgs/flag.png")
question = pygame.image.load("imgs/question.png")

clock = pygame.image.load("imgs/time.png")

# game settings
TITLE = "Minesweeper"

WIDTH = 1280
HEIGHT = 720

FPS = 60

# grid
TILESIZE = 32
GRIDWIDTH = WIDTH/TILESIZE
GRIDHEIGHT = HEIGHT/TILESIZE

# colors
TAN = (234, 219, 198)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
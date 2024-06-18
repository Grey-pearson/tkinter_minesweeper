import pygame, sys
from random import randrange
from pygame.locals import * 
from ctypes import c_int, WINFUNCTYPE, windll
from ctypes.wintypes import HWND, LPCSTR, UINT
def MessageBox(title, text, style):
    return windll.user32.MessageBoxW(0, text, title, style)
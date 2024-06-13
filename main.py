import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Mine_sweeper(ttk.Tk):
    def __init__(self):
        self.board_size = 10
        self.bombs_amount = 13
        self.root = ttk.Window()

    def intro(self):
        pass

    def create_board(self):
        pass
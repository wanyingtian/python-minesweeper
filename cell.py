from tkinter import Button
from tkinter import font as tkFont
import settings
import utils
import math


class Cell:
    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.btn_object = None
        self.x = x
        self.y = y
    
    def create_btn_object(self, frame_location, grid_size = settings.GRID_SIZE):
        btn = Button(
            frame_location,
            width = self.btn_width(grid_size),
            height = self.btn_height(grid_size),
            text = f"{self.x}, {self.y}",
            font = tkFont.Font(family='Helvetica', size=10, weight='bold')

        )
        # assign event to the button
        btn.bind('<Button-1>', self.left_click_actions) #left click
        btn.bind('<Button-3>', self.right_click_actions) # right click
        self.btn_object = btn
    
    def left_click_actions(self, event):
        print(event)
        print("Left Clicked")

    def right_click_actions(self, event):
        print(event)
        print('Right Clicked')
    
    def btn_width(self, grid_size):
        width = math.floor(utils.width_percentage(70) / (8 * grid_size))
        return width
    
    def btn_height(self, grid_size):
        return math.floor(utils.height_percentage(70) / (18 * grid_size))
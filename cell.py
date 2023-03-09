from tkinter import Button
from tkinter import font as tkFont
import random
import math
import settings
import utils



class Cell:
    all = [] #a class attribute that will containn all objects
    #default beginner level
    mine_count = 0
    
    def __init__(self, x, y, level, is_mine = False):
        self.is_mine = is_mine
        self.btn_object = None
        self.x = x
        self.y = y
       
        Cell.level = level
        Cell.mine_count = Cell.total_mine_count()
        #Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, frame_location):
        btn = Button(
            frame_location,
            relief = 'sunken',
            width = 2,
            height = 1
        )
        # assign event to the button
        btn.bind('<Button-1>', self.left_click_actions) #left click
        btn.bind('<Button-3>', self.right_click_actions) # right click
        self.btn_object = btn
    
    def left_click_actions(self, event):
        if self.is_mine:
            self.display_mine()
        else:
            if self.surrounding_mine_count == 0:
                self.display_all_safe()
            self.display_cell()
    
    def display_mine(self):
        # interrupt the game and display that player lost
        self.btn_object.configure(
            bg = 'red',
            text = "!",
            font = tkFont.Font(family='Helvetica', size=10, weight='bold')
            )
    
    def get_cell_by_coordinates(self, x, y):
        # returns cell object based on x, y coordinates
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    @property
    def surrounding_neighbors(self):
        # a propertiy that returns a list of surrounding cells
        # not a method
        neighbors = [
            self.get_cell_by_coordinates(self.x - 1, self.y - 1),
            self.get_cell_by_coordinates(self.x - 1, self.y),
            self.get_cell_by_coordinates(self.x - 1, self.y + 1),
            self.get_cell_by_coordinates(self.x, self.y - 1),
            self.get_cell_by_coordinates(self.x, self.y + 1),
            self.get_cell_by_coordinates(self.x + 1, self.y - 1),
            self.get_cell_by_coordinates(self.x + 1, self.y),
            self.get_cell_by_coordinates(self.x + 1, self.y + 1)
        ]
        neighbors = [cell for cell in neighbors if cell != None]
        return neighbors

    @property
    def surrounding_mine_count(self):
        count = 0
        for neighbor in self.surrounding_neighbors:
            if neighbor.is_mine:
                count += 1
        return count
    
    def display_all_safe(self):
        # display the safe neighbor cells when the clicked cell is 0
        for cell in self.surrounding_neighbors:
            cell.display_cell()

    def display_cell(self):
        # display the number indicating number of mines surrounding the cell
        self.btn_object.configure(
            bg = 'grey',
            text = f"{self.surrounding_mine_count}",
            font = tkFont.Font(family='Helvetica', size=10, weight='bold')
            )

    def right_click_actions(self, event):
        print(event)
        print('Right Clicked')
    
    @staticmethod
    def total_mine_count():
        if Cell.level == 0:
            Cell.mine_count = settings.BEGINNER_MINES_COUNT
        elif Cell.level == 1:
            Cell.mine_count = settings.INTERMEDIATE_MINES_COUNT
        elif Cell.level == 2:
            Cell.mine_count = settings.EXPERT_MINES_COUNT
        return Cell.mine_count

    @staticmethod #method belongs to the class not each individual instance
    def randomize_mines():
        picked_cells = random.sample(Cell.all, Cell.mine_count)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    
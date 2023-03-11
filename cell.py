from tkinter import *
from tkinter import Button
from tkinter import font as tkFont
from tkinter import Label
from tkinter import messagebox as tkMessageBox
from tkinter import PhotoImage
import random
import settings
import ctypes
import sys




class Cell:
    all = [] #a class attribute that will containn all objects
    #default beginner level
    mine_count = 0
    cell_count = 0
    playing = True
    

    def __init__(self, x, y, level, is_mine = False):
        self.is_mine = is_mine
        self.is_clicked = False
        self.is_flagged = False
        self.btn_object = None
        self.x = x
        self.y = y
        self.i = PhotoImage(width=1, height=1)

       
        Cell.level = level
        Cell.mine_count, Cell.cell_count = Cell.difficulty_setting()
        Cell.cell_count_lbl_object = None
        Cell.mine_count_lbl_object = None
        #Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, frame_location):
        self.center_frame = frame_location
        btn = Button(
            frame_location,
            image = self.i,
            compound = 'c',
            relief = 'sunken',
            width = 10,
            height = 10
        )
        # assign event to the button
        btn.bind('<Button-1>', self.left_click_actions) #left click
        btn.bind('<Button-3>', self.right_click_actions) # right click
        self.btn_object = btn
    
    @staticmethod
    def create_cell_count_label(frame_location):
        lbl = Label(
            frame_location,
            bg = 'brown',
            fg = 'white',
            font = tkFont.Font(family='Helvetica', size=10),
            text = f"{Cell.cell_count} cells left"
        )
        Cell.cell_count_lbl_object = lbl
    
    @staticmethod
    def create_mine_count_label(frame_location):
        lbl = Label(
            frame_location,
            bg = 'brown',
            fg = 'white',
            font = tkFont.Font(family='Helvetica', size=10),
            text = f"{Cell.mine_count} mines total"
        )
        Cell.mine_count_lbl_object = lbl

    
    def left_click_actions(self, event):
        
        if self.is_mine:
            self.display_mine()
            self.game_over(False)
        else:
            self.display_cell()
            if Cell.cell_count == Cell.mine_count:
                #show game won
                #ctypes.windll.user32.MessageBoxW(0, 'You Won!', 'You Won', 0)
                self.game_over(True)

    
    def right_click_actions(self, event):
        if (not self.is_flagged) and (not self.is_clicked):
            self.btn_object.configure(
            bg = 'orange',
            text = "?",
            font = tkFont.Font(family='Helvetica', size=10, weight='bold')
            )
            self.is_flagged = True
        elif (self.is_flagged) and (not self.is_clicked):
            self.is_flagged = False
            self.btn_object.configure(
            bg = 'SystemButtonFace',
            text = ""
            ) 

    def display_mine(self):
        # interrupt the game and display that player lost
        self.btn_object.configure(
            bg = 'red',
            text = "!",
            font = tkFont.Font(family='Helvetica', size=10, weight='bold')
            )

    
    def display_neighbors(self):
        # display the safe neighbor cells when the clicked cell is 0
        #self.display_cell()
        for cell in self.surrounding_neighbors:
            cell.display_cell()


    def display_cell(self):
        if not self.is_clicked:
            # display the number indicating number of mines surrounding the cell
            self.btn_object.configure(
                bg = 'grey',
                text = f"{self.surrounding_mine_count}",
                font = tkFont.Font(family='Helvetica', size=10, weight='bold')
            )
            # replace cell count with new count
            Cell.cell_count -= 1
            self.cell_count_lbl_object.configure(
                text = f"{Cell.cell_count} cells left"
            )
            # mark as clicked
            self.is_clicked = True
            self.unbind_event()

            # if count is 0, display surrounding
            if self.surrounding_mine_count == 0:
                self.display_neighbors()



    def game_over(self, won):
        if won:
            msg = "You Win! " 
            res = tkMessageBox.showinfo("Game Over", msg)
                # create window        
        else: 
            msg = "You Lost! "
            res = tkMessageBox.showinfo("Game Over", msg)
        #self.center_frame.destroy()
        self.playing = False
        sys.exit()
        
    
    def restart(self):
        pass

    def unbind_event(self):
        self.btn_object.unbind('<Button-1>')
        self.btn_object.unbind('<Button-3>')
    
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
    
    
    @staticmethod
    def difficulty_setting():
        if Cell.level == 0:
            Cell.mine_count = settings.BEGINNER_MINES_COUNT
            Cell.cell_count = settings.BEGINNER_GRID_SIZE ** 2
        elif Cell.level == 1:
            Cell.mine_count = settings.INTERMEDIATE_MINES_COUNT
            Cell.cell_count = settings.INTERMEDIATE_GRID_SIZE ** 2
        elif Cell.level == 2:
            Cell.mine_count = settings.EXPERT_MINES_COUNT
            Cell.cell_count = settings.EXPERT_HEIGHT * settings.EXPERT_WIDTH
        return Cell.mine_count, Cell.cell_count

    @staticmethod #method belongs to the class not each individual instance
    def randomize_mines():
        picked_cells = random.sample(Cell.all, Cell.mine_count)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    
from tkinter import *
from tkinter import Button
from tkinter import font as tkFont
from tkinter import Label
from tkinter import messagebox as tkMessageBox
from tkinter import PhotoImage
import random
import settings
import utils
import sys
import time
from datetime import time, date, datetime




class Cell:
    all = [] #a class attribute that will containn all objects

    def __init__(self, x, y, level, is_mine = False):
        # initialize each button/cell given coordinates
        self.is_mine = is_mine
        self.is_clicked = False
        self.is_flagged = False
        self.btn_object = None
        self.x = x
        self.y = y
        self.i = PhotoImage(width=1, height=1) # make the buttons square using a blank image
       
        #initialize game settings       
        Cell.level = level
        Cell.mine_count, Cell.cell_count = Cell.difficulty_setting()
        Cell.flag_count = 0
        Cell.cell_count_lbl_object = None
        Cell.mine_count_lbl_object = None
        Cell.flag_count_lbl_object = None
        Cell.timer_lbl_object = None
        Cell.start_time = None
        Cell.ts = '00:00:00'
        Cell.playing = True
        #Append the object/cell to the Cell.all list
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

    def left_click_actions(self, event):
        # start timer if not already
        if Cell.start_time == None:
            Cell.start_time = datetime.now()
            Cell.update_timer()
        # display cell/mine
        if self.is_mine:
            Cell.playing = False
            self.display_mine() #show mine
            self.game_over(False) # show game lost
        else:
            self.display_cell()
            # win if leftover cells are all mines
            if Cell.cell_count == Cell.mine_count:                
                Cell.playing = False #playing stopped
                self.game_over(True) #show game won                 
  
    def right_click_actions(self, event):
        # start timer if not already
        if Cell.start_time == None:
            Cell.start_time = datetime.now()
            Cell.update_timer()
        # flag/unflag cells
        if (not self.is_flagged) and (not self.is_clicked):
            self.btn_object.configure(
            bg = 'orange',
            text = "?",
            font = tkFont.Font(family='Helvetica', size=10, weight='bold')
            )
            self.is_flagged = True
            Cell.flag_count += 1
            self.flag_count_lbl_object.configure(
                text = f"Flags: {Cell.flag_count}"
                )
        elif (self.is_flagged) and (not self.is_clicked):
            self.is_flagged = False
            self.btn_object.configure(
            bg = 'SystemButtonFace',
            text = ""
            ) 
            Cell.flag_count -= 1
            self.flag_count_lbl_object.configure(
                text = f"Flags: {Cell.flag_count}"
                )

    def display_mine(self):
        self.btn_object.configure(
            bg = 'red',
            text = "!",
            font = tkFont.Font(family='Helvetica', size=10, weight='bold')
            )
    
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
            if self.is_flagged:
                Cell.flag_count -= 1
                self.flag_count_lbl_object.configure(
                text = f"Flags: {Cell.flag_count}"
                )
                self.is_flagged = False
            # if count is 0, display surrounding
            if self.surrounding_mine_count == 0:
                self.display_neighbors()

    def display_neighbors(self):
        # display the safe neighboring cells when the clicked cell is 0
        for cell in self.surrounding_neighbors:
            cell.display_cell()

    def game_over(self, won):
        # display win/lose message and ask if restart
        if won:
            msg = f"""  
            You won! 
            Time used: {Cell.ts}
            Play again?
            """
            res = tkMessageBox.askyesno("Game Over", msg)        
        else: 
            msg = "You Lost :( Play again?"
            res = tkMessageBox.askyesno("Game Over", msg)
        if res:
            self.restart()
        else:
            sys.exit()        
    
    def restart(self):
        # delete cells and zero all values, 
        for cell in Cell.all:
            del cell
        Cell.all = [] 
        Cell.mine_count = 0
        Cell.cell_count = 0
        Cell.flag_count = 0
        Cell.playing = False

        # ask for user selection for difficulty
        self.restart_msg = Label(
            self.center_frame,
            bg = 'brown',
            fg = 'white',
            text =
            """

            Click any level to restart the game!          

            """,
            font = ('Calibri',18)
        )
        self.restart_msg.place(
            relwidth = 0.8,
            relheight = 0.4,
            x = utils.width_percentage(10),
            y = utils.height_percentage(20)
        )
        
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
        # return count of surrounding mines
        count = 0
        for neighbor in self.surrounding_neighbors:
            if neighbor.is_mine:
                count += 1
        return count
    
    @staticmethod
    def create_cell_count_label(frame_location):
        # counts # of cells left
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
        # display total mines
        lbl = Label(
            frame_location,
            bg = 'brown',
            fg = 'white',
            font = tkFont.Font(family='Helvetica', size=10),
            text = f"Total mines:{Cell.mine_count}"
        )
        Cell.mine_count_lbl_object = lbl

    @staticmethod
    def create_flag_count_label(frame_location):
        # counts number of flags
        lbl = Label(
            frame_location,
            bg = 'brown',
            fg = 'white',
            font = tkFont.Font(family='Helvetica', size=10),
            text = f"Flags: {Cell.flag_count}"
        )
        Cell.flag_count_lbl_object = lbl
    
    @staticmethod
    def create_timer_label(frame_location):
        lbl = Label(
            frame_location,
            bg = 'brown',
            fg = 'white',
            font = tkFont.Font(family='Helvetica', size=10),
            text = f"Timer: 00:00:00"
        )
        Cell.timer_lbl_object = lbl

    @staticmethod
    def update_timer():
        if Cell.start_time == None or Cell.playing == False:
            pass
        elif Cell.start_time != None:
            delta = datetime.now() - Cell.start_time
            Cell.ts = str(delta).split('.')[0] # drop ms
            if delta.total_seconds() < 36000:
                Cell.ts = "0" + Cell.ts # zero-pad
        Cell.timer_lbl_object.config(text = f"Timer: {Cell.ts}")
        Cell.timer_lbl_object.after(100, Cell.update_timer)
   
    @staticmethod
    def difficulty_setting():
        # define number of cells and mines based on difficulty
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

    @staticmethod 
    def randomize_mines():
        picked_cells = random.sample(Cell.all, Cell.mine_count)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    
from tkinter import * #import everything from tkinter
from tkinter import messagebox as tkMessageBox
from cell import Cell
import settings
import utils

'''
Creating Cells and Mines
Create a cell class in cell.py that can build cells with clickable buttons
the cell button objects would also have actions when left or right clicked
'''





class Game:

    def __init__(self, root):
        self.root = root
        self.difficulty = 0

        self.game_window()
        
    def reset(self):
        self.center_frame.destroy()
        self.game_window()
        self.construct_cells()
        Cell.randomize_mines()
        #Create cell count label from Cell Class
        Cell.create_cell_count_label(self.top_frame)
        Cell.cell_count_lbl_object.place(x = 10, y = 10)
  

    def beginner(self):
        msg = "Are you sure you want to start the game in Beginner level? " 
        res = tkMessageBox.askyesno("Restart", msg)
        if res:
            self.difficulty = 0
            print(self.difficulty)
            self.reset()
        else:
            pass
        
    def intermediate(self):
        msg = "Are you sure you want to start the game in Intermediate level? " 
        res = tkMessageBox.askyesno("Restart", msg)
        if res:
            self.difficulty = 1
            print(self.difficulty)
            self.reset()
        else:
            pass
        
    def expert(self):
        msg = "Are you sure you want to restart the game in Expert level? " 
        res = tkMessageBox.askyesno("Restart", msg)
        if res:
            self.difficulty = 2
            print(self.difficulty)
            self.reset()
        else:
            pass
        
    def game_window(self):
        self.root.configure(bg = "beige")
        self.root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') # window size width x height
        self.root.title("Chris's Minesweeper Game")
        # to avoid resize window, uncomment line below
        self.root.resizable(False,False)
        
        self.top_frame = Frame(
            self.root,
            bg = 'brown',
            width = utils.width_percentage(100),
            height = utils.height_percentage(20)
        )
        self.top_frame.place(x = 0, y = 0) # where the top left frame starts

        self.center_frame = Frame(
            self.root,
            bg = 'beige',
            width = utils.width_percentage(100),
            height = utils.height_percentage(80)
        )
        self.center_frame.place(relwidth = 1, relheight = 0.8, x = utils.width_percentage(0), y = utils.height_percentage(20))

        self.game_title = Label(
            self.top_frame,
            bg = 'brown',
            fg = 'white',
            text ="Chris's Minesweeper Game" ,
            font = ('Calibri',18)
        )
        self.game_title.place(
            x = utils.width_percentage(25),
            y = utils.width_percentage(5)
        )

        level0 = Button(self.top_frame, text = "Beginner", command = self.beginner)
        level1 = Button(self.top_frame, text = "Intermediate", command = self.intermediate)
        level2 = Button(self.top_frame, text = "Expert", command = self.expert)

        level0.place(x = utils.width_percentage(25), y = utils.height_percentage(15))
        level1.place(x = utils.width_percentage(50), y = utils.height_percentage(15))
        level2.place(x = utils.width_percentage(75), y = utils.height_percentage(15))

    def construct_cells(self):
        if self.difficulty == 0:
            grid_width = settings.BEGINNER_GRID_SIZE
            grid_height = settings.BEGINNER_GRID_SIZE   
        elif self.difficulty == 1:
            grid_width = settings.INTERMEDIATE_GRID_SIZE
            grid_height = settings.INTERMEDIATE_GRID_SIZE
        elif self.difficulty == 2:
            grid_width = settings.EXPERT_WIDTH
            grid_height = settings.EXPERT_HEIGHT

        for x in range(grid_width):
            Grid.rowconfigure(self.center_frame, x, weight=1)
            for y in range(grid_height):
                Grid.columnconfigure(self.center_frame, y, weight=1)
                c = Cell(x, y, self.difficulty)
                c.create_btn_object(self.center_frame)
                c.btn_object.grid(column = x, row = y, padx = 1, pady =1,sticky = N+S+E+W)






'''
Cell.randomize_mines()
#Create cell count label from Cell Class
Cell.create_cell_count_label(top_frame)
Cell.cell_count_lbl_object.place(x = 10, y = 10)
'''



def main():
    # create window
    root = Tk()
    # build game window
    g = Game(root) 
    # Run the window
    root.mainloop() 

if __name__ == "__main__":
    main()





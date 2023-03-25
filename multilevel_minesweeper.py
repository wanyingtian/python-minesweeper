from tkinter import * #import everything from tkinter
from tkinter import messagebox as tkMessageBox
from cell import Cell # import Cell class
import settings
import utils

class Game:

    def __init__(self, root):
        self.root = root
        self.difficulty = 0
        self.setup()

    def setup(self):
        self.game_window()
        self.construct_cells()
        Cell.randomize_mines()
        # Create labels from Cell Class that display game info:
        Cell.create_cell_count_label(self.top_frame) # number of cells left
        Cell.cell_count_lbl_object.place(x = 5, y = 10)
        Cell.create_mine_count_label(self.top_frame) # total number of mines
        Cell.mine_count_lbl_object.place(x = 5, y = 30)
        Cell.create_flag_count_label(self.top_frame) # number of flags
        Cell.flag_count_lbl_object.place(x = 5, y = 50)
        Cell.create_timer_label(self.top_frame)
        Cell.timer_lbl_object.place(x = 5, y = 70)

    def reset(self):
        self.center_frame.destroy()
        # delete all cells and zero all data
        for cell in Cell.all:
            del cell
        Cell.all = [] 
        Cell.mine_count = 0
        Cell.cell_count = 0
        Cell.flag_count = 0
        self.setup()
  
    def construct_cells(self):
        #define game setting based on difficulty selection
        if self.difficulty == 0:
            grid_width = settings.BEGINNER_GRID_SIZE
            grid_height = settings.BEGINNER_GRID_SIZE   
        elif self.difficulty == 1:
            grid_width = settings.INTERMEDIATE_GRID_SIZE
            grid_height = settings.INTERMEDIATE_GRID_SIZE
        elif self.difficulty == 2:
            grid_width = settings.EXPERT_WIDTH
            grid_height = settings.EXPERT_HEIGHT
        #construct cells using Cell class
        for x in range(grid_width):
            Grid.rowconfigure(self.center_frame, x, weight=1)
            for y in range(grid_height):
                Grid.columnconfigure(self.center_frame, y, weight=1)
                c = Cell(x, y, self.difficulty)
                c.create_btn_object(self.center_frame)
                c.btn_object.grid(column = x, row = y, padx = 1, pady =1,sticky = N+S+E+W)

    def beginner(self):
        msg = "Want to start at Beginner level? " 
        res = tkMessageBox.askyesno("Restart", msg)
        if res:
            self.difficulty = 0
            self.reset()
        else:
            pass

    def intermediate(self):
        msg = "Want to start at Intermediate level? " 
        res = tkMessageBox.askyesno("Restart", msg)
        if res:
            self.difficulty = 1
            self.reset()
        else:
            pass
        
    def expert(self):
        msg = "Want to start at Expert level? " 
        res = tkMessageBox.askyesno("Restart", msg)
        if res:
            self.difficulty = 2
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
            y = utils.height_percentage(5)
        )

        self.level0 = Button(
            self.top_frame, 
            text = "Beginner", 
            font = ('Helvetica', 10, 'bold'),
            command = self.beginner
            )
        self.level1 = Button(
            self.top_frame, 
            text = "Intermediate",
            font = ('Helvetica', 10, 'bold'), 
            command = self.intermediate
            )
        self.level2 = Button(
            self.top_frame, 
            text = "Expert", 
            font = ('Helvetica', 10, 'bold'),
            command = self.expert
            )

        self.level0.place(x = utils.width_percentage(25), y = utils.height_percentage(15))
        self.level1.place(x = utils.width_percentage(45), y = utils.height_percentage(15))
        self.level2.place(x = utils.width_percentage(70), y = utils.height_percentage(15))
### End of Game Class

def main():
    # create window
    root = Tk()
    # build game window
    g = Game(root) 
    # Run the window
    root.mainloop()

if __name__ == "__main__":
    main()





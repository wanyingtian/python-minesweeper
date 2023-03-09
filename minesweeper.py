from tkinter import * #import everything from tkinter
from cell import Cell
import settings
import utils

root = Tk() # create window
'''
GUI Window and Frames:
There will be 3 main frames, 
one on top for the title, 
one on the left as a side bar, 
and one in the center for the mine grid
'''

root.configure(bg = "beige")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') # window size width x height
root.title("Chris's Minesweeper Game")
# to avoid resize window, uncomment line below
root.resizable(False,False)

top_frame = Frame(
    root,
    bg = 'brown',
    width = utils.width_percentage(100),
    height = utils.height_percentage(20)
)
top_frame.place(x = 0, y = 0) # where the top left frame starts
#top_frame.grid(column = 0, row = 0,sticky=N)
'''
left_frame = Frame(
    root,
    bg = 'tan',
    width= utils.width_percentage(20),
    height = utils.height_percentage(100)    
)
left_frame.place(x = 0, y = utils.height_percentage(20))
'''
center_frame = Frame(
    root,
    bg = 'beige',

    width = utils.width_percentage(100),
    height = utils.height_percentage(80)
)
center_frame.place(relwidth = 1, relheight = 0.8, x = utils.width_percentage(0), y = utils.height_percentage(20))
#center_frame.grid(row=1, column=0, sticky=N+S+E+W)
'''
Creating Cells and Mines
Create a cell class in cell.py that can build cells with clickable buttons
the cell button objects would also have actions when left or right clicked
'''
difficulty = 1
def construct_cells(difficulty):
    if difficulty == 0:
        grid_width = settings.BEGINNER_GRID_SIZE
        grid_height = settings.BEGINNER_GRID_SIZE
    elif difficulty == 1:
        grid_width = settings.INTERMEDIATE_GRID_SIZE
        grid_height = settings.INTERMEDIATE_GRID_SIZE
    elif difficulty == 2:
        grid_width = settings.EXPERT_WIDTH
        grid_height = settings.EXPERT_HEIGHT

    for x in range(grid_width):
        Grid.rowconfigure(center_frame, x, weight=1)
        for y in range(grid_height):
            Grid.columnconfigure(center_frame, y, weight=1)
            c = Cell(x, y, difficulty)
            c.create_btn_object(center_frame)
            c.btn_object.grid(column = x, row = y, sticky = N+S+E+W) 

construct_cells(difficulty)
Cell.randomize_mines()

# Run the window
root.mainloop() 

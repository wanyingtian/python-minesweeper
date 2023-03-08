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
    width = settings.WIDTH,
    height = utils.height_percentage(25)
)
top_frame.place(x = 0, y = 0) # where the top left frame starts

left_frame = Frame(
    root,
    bg = 'tan',
    width= utils.width_percentage(20),
    height = utils.height_percentage(75)    
)
left_frame.place(x = 0, y = utils.height_percentage(25))

center_frame = Frame(
    root,
    bg = 'beige',
    width = utils.width_percentage(80),
    height = utils.height_percentage(75)
)
center_frame.place(x = utils.width_percentage(20), y = utils.height_percentage(25))

'''
Creating Cells and Mines
Create a cell class in cell.py that can build cells with clickable buttons
the cell button objects would also have actions when left or right clicked
'''
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(center_frame)
        c.btn_object.grid(column = x, row = y) # notice grid(column and row) are used

# Run the window
root.mainloop() 

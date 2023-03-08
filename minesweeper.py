from tkinter import * #import everything from tkinter
import settings
import utils

root = Tk() # create window

root.configure(bg = "beige")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') # window size width x height
root.title("Chris's Minesweeper Game")
# to avoid resize window, uncomment line below
root.resizable(False,False)
'''
Frames:
There will be 3 main frames, 
one on top for the title, 
one on the left as a side bar, 
and one in the center for the mine grid
'''
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
# Run the window
root.mainloop() 

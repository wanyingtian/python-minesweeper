from tkinter import Button

class Cell:
    def __init__(self, is_mine = False):
        self.is_mine = is_mine
        self.btn_object = None
    
    def create_btn_object(self, frame_location):
        btn = Button(
            frame_location,
            text = "a cute button"
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
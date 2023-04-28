import os 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

class Register:

    def __init__(self,root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1080x720+0+0")

if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()


import os 
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

class Register:

    def __init__(self,root):
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1080x720+0+0")

        self.back = ImageTk.PhotoImage(file='images/register.jpg')
        reg_bg = Label(self.root, image = self.back)
        reg_bg.place(x=0,y=0,relwidth=1,relheight=1)
        

        frame = Frame(self.root,bg='white',highlightthickness=0)
        frame.place(x=200,y=150,width=650,height=450)

if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()


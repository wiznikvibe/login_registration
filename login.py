import os 
from tkinter import *
from PIL import Image, ImageTk

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry("500x500+0+0")
        

        self.background = ImageTk.PhotoImage(file='images/background.jpg')
        lb_bg = Label(self.root, image = self.background)
        lb_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root,bg='white',highlightthickness=5,border=2)
        frame.place(x=150,y=100,width=200,height=300)

        img1 = Image.open('images/login.png')
        img1 = img1.resize((50,50),Image.Resampling.LANCZOS)
        self.log_img = ImageTk.PhotoImage(img1)
        lab_img = Label(image=self.log_img,bg='white',borderwidth=5)
        lab_img.place(x=225,y=85)

        log_in = Label(frame, text="Login", font=('Arial',17,'bold'),bg='white')
        log_in.place(x=70,y=35)

        user_lab = Label(frame, text="Username:", font=('Arial',10,'normal'),bg='white')
        user_lab.place(x=10, y=75)

        
        pass_lab = Label(frame, text="Password:", font=('Arial',10,'normal'),bg='white')
        pass_lab.place(x=10, y=125)
        
        
        user_entry = Entry(frame, font=('Arial',10,'normal'),bg='white')
        user_entry.place(x=1,y=95, width=182)
        pass_entry = Entry(frame, font=('Arial',10,'normal'),bg='white')
        pass_entry.place(x=1,y=145, width=182)






if __name__ == '__main__':
    root = Tk()
    app = Login_window(root)
    root.mainloop()
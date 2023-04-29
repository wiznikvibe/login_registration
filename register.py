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

        register_lab = Label(frame,text="Register",font=('Arial',22,'bold'),bg='white')
        register_lab.place(x=20,y=20)

        #-------------- Label and Entry --------------#
        fname = Label(frame,text='First Name',font=('Arial',12,'bold'),bg='white')
        fname.place(x=20,y=80)
        fname_entry = Entry(frame, font=('Arial',12,'normal'),bg='white')
        fname_entry.place(x=20,y=100,width=250)

        lname = Label(frame,text='Last Name',font=('Arial',12,'bold'),bg='white')
        lname.place(x=300,y=80)
        lname_entry = Entry(frame, font=('Arial',12,'normal'),bg='white')
        lname_entry.place(x=300,y=100,width=250)

        cont = Label(frame,text='Contact',font=('Arial',12,'bold'),bg='white')
        cont.place(x=20,y=130)
        cont_entry = Entry(frame, font=('Arial',12,'normal'),bg='white')
        cont_entry.place(x=20,y=150,width=250)

        mail = Label(frame,text='Email',font=('Arial',12,'bold'),bg='white')
        mail.place(x=300,y=130)
        mail_entry = Entry(frame, font=('Arial',12,'normal'),bg='white')
        mail_entry.place(x=300,y=150,width=250)

        sec_ques = Label(frame,text='Select Security Question:',font=('Arial',12,'bold'),bg='white')
        sec_ques.place(x=20,y=180)


        sec_ans = Label(frame,text='Security Answer:',font=('Arial',12,'bold'),bg='white')
        sec_ans.place(x=300,y=180)


        sec_ques = Label(frame,text='Password',font=('Arial',12,'bold'),bg='white')
        sec_ques.place(x=20,y=250)


        sec_ques = Label(frame,text='Confirm Password',font=('Arial',12,'bold'),bg='white')
        sec_ques.place(x=300,y=250)

if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()


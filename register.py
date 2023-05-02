import os 
import configparser
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector



config = configparser.ConfigParser()
config.read('config.ini')
HOST = config['identity']['host']
USER = config['identity']['user']
PASSWORD = config['identity']['password']
PORT = config['identity']['port']
DATABASE = config['identity']['database']

class Register:

    def __init__(self,root):

        # Window 
        self.root = root
        self.root.title('Registration Form')
        self.root.geometry("1080x720+0+0")

        # Variables 
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_cont = StringVar()
        self.var_mail = StringVar()
        self.var_sec_ques = StringVar()
        self.var_sec_ans = StringVar()
        self.var_pass = StringVar()
        self.var_pass_con = StringVar()
        



        # background Image 
        self.back = ImageTk.PhotoImage(file='images/register.jpg')
        reg_bg = Label(self.root, image = self.back)
        reg_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        # Frame- Registeration Form 
        frame = Frame(self.root,bg='white',highlightthickness=0)
        frame.place(x=200,y=150,width=650,height=450)

        register_lab = Label(frame,text="Register",font=('Arial',22,'bold'),bg='white')
        register_lab.place(x=20,y=20)

        #-------------- Label and Entry --------------#
        # First Name 
        fname = Label(frame,text='First Name',font=('Arial',12,'bold'),bg='white')
        fname.place(x=20,y=80)
        fname_entry = Entry(frame, textvariable=self.var_fname, font=('Arial',12,'normal'),bg='white')
        fname_entry.place(x=20,y=100,width=250)

        # Last Name 
        lname = Label(frame,text='Last Name',font=('Arial',12,'bold'),bg='white')
        lname.place(x=300,y=80)
        lname_entry = Entry(frame, textvariable=self.var_lname, font=('Arial',12,'normal'),bg='white')
        lname_entry.place(x=300,y=100,width=250)

        # Contact
        cont = Label(frame,text='Contact',font=('Arial',12,'bold'),bg='white')
        cont.place(x=20,y=130)
        cont_entry = Entry(frame, textvariable=self.var_cont, font=('Arial',12,'normal'),bg='white')
        cont_entry.place(x=20,y=150,width=250)

        # Mail
        mail = Label(frame,text='Email',font=('Arial',12,'bold'),bg='white')
        mail.place(x=300,y=130)
        mail_entry = Entry(frame, textvariable=self.var_mail, font=('Arial',12,'normal'),bg='white')
        mail_entry.place(x=300,y=150,width=250)

        # Security Question / Answer
        sec_ques = Label(frame,text='Select Security Question:',font=('Arial',12,'bold'),bg='white')
        sec_ques.place(x=20,y=180)
        self.sec_ques_options = ttk.Combobox(frame, textvariable=self.var_sec_ques, font=('Arial',12,'bold'))
        self.sec_ques_options['values']=('Select','Your Birth Place?','Name of First Pet?','City you were born in?')
        self.sec_ques_options.place(x= 20,y=200,width=250)

        sec_ans = Label(frame,text='Security Answer:',font=('Arial',12,'bold'),bg='white')
        sec_ans.place(x=300,y=180)
        sec_entry = Entry(frame, textvariable=self.var_sec_ans,  font=('Arial',12,'normal'),bg='white')
        sec_entry.place(x=300,y=200,width=250)

        # Password 
        pas_lab = Label(frame,text='Password',font=('Arial',12,'bold'),bg='white')
        pas_lab.place(x=20,y=250)
        pas_entry = Entry(frame, textvariable=self.var_pass,  font=('Arial',12,'normal'),bg='white')
        pas_entry.place(x=20,y=270,width=250)

        # Confirm Password 
        con_pas = Label(frame,text='Confirm Password',font=('Arial',12,'bold'),bg='white')
        con_pas.place(x=300,y=250)
        conpas_entry = Entry(frame, textvariable=self.var_pass_con,  font=('Arial',12,'normal'),bg='white')
        conpas_entry.place(x=300,y=270,width=250)

        # Check Terms and Conditions
        self.var_check = IntVar() 
        term_check = Checkbutton(frame, variable=self.var_check, onvalue=1, offvalue=0,  text='I have read and Accept the Terms and Conditions.',font=('Arial',8,'bold'))
        term_check.place(x=20,y=300)

        # Register Button
        register = Image.open(r'images\register.png')
        img = register.resize((200,75),Image.Resampling.LANCZOS)
        self.register_img = ImageTk.PhotoImage(img)
        reg_img = Button(frame, command=self.register_data, image=self.register_img, borderwidth=0, bg='white')
        reg_img.place(x=20,y=340,width=125,height=35)

        # Login Button
        flog = Image.open(r'images\wogin.png')
        img1 = flog.resize((100,25),Image.Resampling.LANCZOS)
        self.flog_img = ImageTk.PhotoImage(img1)
        flog_img = Button(frame,image=self.flog_img,borderwidth=0,bg='white')
        flog_img.place(x=150,y=340,width=100,height=35)


        # ----------------- Functions ---------------------
    # def create_server_connection(self,host_name,user_name,user_password):
    #     self.conn = None
    #     try:
    #         self.conn = mysql.connector.connect(
    #             host = self.host_name,
    #             user = self.user_name,
    #             password = self.user_password 
    #         )
    #         print("MySql Database connection successful")
    #     except Exception as e:
    #         print(e)
        
    #     return conn
            
    def register_data(self):
        if self.var_fname.get()=='' or self.var_mail.get()=='' or self.var_sec_ques.get()=='':
            messagebox.showerror('Missing data','You have missed the important fields.')
        elif self.var_pass.get() != self.var_pass_con.get():
            messagebox.showerror('Error','Password must be same!')
        elif self.var_check.get()==0:
            messagebox.showerror('Error',"Please Read the Terms and Acknowledge the conditions")
        else:
            try:
            # connection = self.create_server_connection(config.get('identity', 'host'),config.get('identity', 'user'),config.get('identity', 'password'))
                conn = mysql.connector.connect(host=HOST,user=USER,password=PASSWORD,database=DATABASE,port=PORT)
                my_cursor = conn.cursor()
                query = ("select * from user_data where email=%s")
                value=(self.var_mail.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                if row != None:
                    messagebox.showerror('Error','User already exits, please try another email')
                else:
                    my_cursor.execute('insert into user_data values(%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                self.var_fname.get(),
                                                                                                self.var_lname.get(),
                                                                                                self.var_cont.get(),
                                                                                                self.var_mail.get(),
                                                                                                self.var_sec_ques.get(),
                                                                                                self.var_sec_ans.get(),
                                                                                                self.var_pass.get(),
                                                                                                )
                                                                                                    )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registration is Complete.")
            except Exception as e:
                print(e)
                 



if __name__ == '__main__':
    root = Tk()
    app = Register(root)
    root.mainloop()


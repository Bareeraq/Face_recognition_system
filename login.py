from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import time 
import datetime
import mysql.connector
# from main import Face_Recognition_System

# def main():
#     win = Tk()
#     app=Login_Window(win)
#     win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        img = Image.open(r"Project imgs\2.jpg")
        img = img.resize((1530,790), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(img)

        lbl_bg = Label(self.root, image = self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame= Frame(self.root, bg="bisque1")
        frame.place(x=500, y=160, width=400, height=460)

        img1=Image.open(r"Project imgs\user.png")
        img1=img1.resize((150,70), Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img1)

        lblimg1= Label(image=self.photoimage, bg="black", borderwidth=0)
        lblimg1.place(x=500, y=160, width=400, height=100)

        get_str= Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="bisque1")
        get_str.place(x=130, y=100)

        #labels
        username=lbl= Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="bisque1")
        username.place(x=40, y=155)

        self.txtuser= ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=40, y=180, width=320)

        password=lbl= Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="bisque1")
        password.place(x=40, y=220)

        self.txtpass= ttk.Entry(frame, font=("times new roman", 15))
        self.txtpass.place(x=40, y=245, width=320)

        # Login Button
        loginbtn= Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="White", bg="Black", activeforeground="White", activebackground="Black")
        loginbtn.place(x=95, y=290, width=200, height=40)

        # Register Button
        registerbtn= Button(frame, text="New User? Register", font=("times new roman", 12, "bold"), borderwidth=0, fg="Black", bg="Bisque1", activeforeground="Black", activebackground="Bisque1")
        registerbtn.place(x=0, y=340, width=210)

        #Forgot Password Button
        forgotbtn= Button(frame, text="Forgot Password?", font=("times new roman", 12, "bold"), borderwidth=0, fg="Black", bg="bisque1", activeforeground="black", activebackground="bisque1")
        forgotbtn.place(x=0, y=365, width=200)

    def login(self):
               
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.txtuser.get()=="bareera" and self.txtpass.get()==bareera@21:
            messagebox.showinfo("Success!", "Welcome to Face Recognition System!")
        else:
            messagebox.showerror("Invalid", "Incorrect username or password")

if __name__ == "__main__":
            root = Tk()
            obj = Login_Window(root)
            root.mainloop()
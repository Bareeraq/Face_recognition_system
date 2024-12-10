from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text = "FACE RECOGNITION", font=("georgia", 35,"bold"), bg= "black", fg="white")
        title_lbl.place(x=0, y=0, width= 1400, height= 45)

        img_backgd = Image.open(r"Project imgs\face_detect_bg.jpg")
        img_backgd = img_backgd.resize((1400,705), Image.LANCZOS)
        self.photoimg_backgd = ImageTk.PhotoImage(img_backgd)

        bg_img = Label(self.root, image = self.photoimg_backgd)
        bg_img.place(x=0, y=46, width= 1400, height= 705)
        
        b1_1= Button(self.root, text= "TRAIN DATA", command=self.train_classifier, cursor= "hand2", font=("georgia", 13,"bold"), bg= "black", fg="white")
        b1_1.place(x=0, y=350, width= 1400, height= 54)









if __name__ == "__main__":
    root=Tk()
    obj= Face_Recognition(root)
    root.mainloop()
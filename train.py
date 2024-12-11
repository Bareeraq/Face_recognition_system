from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text = "TRAIN DATASET", font=("georgia", 35,"bold"), bg= "black", fg="white")
        title_lbl.place(x=0, y=0, width= 1400, height= 45)

        img_backgd = Image.open(r"Project imgs\2.jpg")
        img_backgd = img_backgd.resize((1400,705), Image.LANCZOS)
        self.photoimg_backgd = ImageTk.PhotoImage(img_backgd)

        bg_img = Label(self.root, image = self.photoimg_backgd)
        bg_img.place(x=0, y=46, width= 1400, height= 705)

        #button
        b1_1= Button(self.root, text= "TRAIN DATA", command=self.train_classifier, cursor= "hand2", font=("georgia", 13,"bold"), bg= "black", fg="white")
        b1_1.place(x=0, y=350, width= 1400, height= 54)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]
        
        for image in path:
            img= Image.open(image).convert('L') #grayscale image
            imageNp= np.array(img, 'uint8')
            id= int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ================Train the classifier and save==================== 
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")


if __name__ == "__main__":
    root=Tk()
    obj= Train(root)
    root.mainloop()
import cv2
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from dotenv import load_dotenv

load_dotenv()

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("georgia", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        # Background image
        img_backgd = Image.open(r"Project imgs\face_detect_bg.jpg")
        img_backgd = img_backgd.resize((1400, 705), Image.LANCZOS)
        self.photoimg_backgd = ImageTk.PhotoImage(img_backgd)

        bg_img = Label(self.root, image=self.photoimg_backgd)
        bg_img.place(x=0, y=46, width=1400, height=705)

        # Detect Face Button
        b1_1 = Button(bg_img, text="DETECT FACE", cursor="hand2", command=self.face_recog, font=("georgia", 13, "bold"),
                      bg="black", fg="white")
        b1_1.place(x=0, y=350, width=1400, height=54)

    #=====================Attendance=====================================
    def mark_attendance(self, i, n, p, s):
        with open("bareera.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry= line.split((","))  #bareera,2,B.tech,SCSE
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (p not in name_list) and (s not in name_list)):
                now= datetime.now()
                d1= now.strftime("%d/%m/%Y")
                dtString= now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{p},{s},{dtString},{d1},Present")    

    #====================Face Recognition===================================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []  # Empty list

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                face_region = gray_image[y:y + h, x:x + w]
                face_region = np.array(face_region, dtype=np.uint8)

                id, predict = clf.predict(face_region)
                confidence = int(100 * (1 - predict / 300))

                # Debugging print statements
                print(f"ID: {id}, Confidence: {confidence}")

                # Get database credentials
                db_host = os.getenv("DB_HOST")
                db_username = os.getenv("DB_USERNAME")
                db_password = os.getenv("DB_PASSWORD")
                db_database = os.getenv("DB_DATABASE")

                if not all([db_host, db_username, db_password, db_database]):
                    print("Error: Missing database credentials in .env")
                    return

                try:
                    # Establish a database connection
                    conn = mysql.connector.connect(
                        host=db_host,
                        username=db_username,
                        password=db_password,
                        database=db_database
                    )
                    my_cursor = conn.cursor()

                    # Use parameterized queries to avoid SQL injection

                    my_cursor.execute("SELECT `Student Id` FROM student WHERE `Student Id` = %s", (id,))
                    i = my_cursor.fetchone()
                    i = "Unknown" if i is None else "+".join(i)

                    my_cursor.execute("SELECT `Student Name` FROM student WHERE `Student Id` = %s", (id,))
                    n = my_cursor.fetchone()
                    print(f"Fetched Name: {n}")  # Debugging line
                    n = "Unknown" if n is None else "+".join(n)

                    my_cursor.execute("SELECT Program FROM student WHERE `Student Id` = %s", (id,))
                    p = my_cursor.fetchone()
                    print(f"Fetched Program: {p}")  # Debugging line
                    p = "Unknown" if p is None else "+".join(p)

                    my_cursor.execute("SELECT School FROM student WHERE `Student Id` = %s", (id,))
                    s = my_cursor.fetchone()
                    print(f"Fetched School: {s}")  # Debugging line
                    s = "Unknown" if s is None else "+".join(s)
                   
                    # Show data if confidence is high
                    if confidence > 70:  # confidence threshold
                        cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Program: {p}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"School: {s}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        self.mark_attendance(i,n,p,s)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                finally:
                    conn.close()

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        # Initialize Cascade Classifier
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        # Load Pretrained Classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition System", img)

            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

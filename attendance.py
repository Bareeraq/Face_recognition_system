from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from dotenv import load_dotenv
import os
load_dotenv()

class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #bg img
        img = Image.open(r"Project imgs\2.jpg")
        img = img.resize((1530,790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image = self.photoimg)
        bg_img.place(x = 0, y= 0, width = 1400, height = 790)

        title_lbl = Label(bg_img, text = "ATTENDANCE MANAGEMENT SYSTEM", font=("georgia", 35,"bold"), bg= "black", fg="white")
        title_lbl.place(x=0, y=0, width= 1400, height= 45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1320, height=670)

        #LEFT FRAME
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font = ("georgia", 14, "bold"))
        Left_frame.place(x=10, y=10, width=640, height=645)

        img_left = Image.open(r"Project imgs\3.jpg")
        img_left = img_left.resize((632,140), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img = Label(Left_frame, image = self.photoimg_left)
        bg_img.place(x=1, y=0, width= 634, height= 130)

        left_inside_frame = Frame(Left_frame , bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=4, y=135, width=628, height=480)

        #Labels and entries
        #Attendance Id
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("georgia", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, width=14, font=("georgia", 12))
        attendanceId_entry.grid(row=0, column=1, pady=5, sticky=W)
        
        #Student ID
        IdLabel = Label(left_inside_frame, text="Id:", font=("georgia", 12, "bold"), bg="white")
        IdLabel.grid(row=0, column=2, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, width=14, font=("georgia", 12))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        #Name
        nameLabel = Label(left_inside_frame, text="Name:", font=("georgia", 12, "bold"), bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, width=14, font=("georgia", 12))
        name_entry.grid(row=1, column=1, pady=8, sticky=W)
        
        #Program
        programLabel = Label(left_inside_frame, text="Program:", font=("georgia", 12, "bold"), bg="white")
        programLabel.grid(row=1, column=2)

        program_entry = ttk.Entry(left_inside_frame, width=14, font=("georgia", 12))
        program_entry.grid(row=1, column=3, padx=10, pady=8, sticky=W)
        
        #date
        dateLabel = Label(left_inside_frame, text="Date:", font=("georgia", 12, "bold"), bg="white")
        dateLabel.grid(row=2, column=0, padx=10, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=14, font=("georgia", 12))
        date_entry.grid(row=2, column=1, pady=8, sticky=W)

        #time
        timeLabel = Label(left_inside_frame, text="Time:", font=("georgia", 12, "bold"), bg="white")
        timeLabel.grid(row=2, column=2, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=14, font=("georgia", 12))
        time_entry.grid(row=2, column=3, padx=10, pady=8, sticky=W)

        #attendance Status
        attendanceLabel = Label(left_inside_frame, text="Attendance Status:", font=("georgia", 12, "bold"), bg="white")
        attendanceLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status= ttk.Combobox(left_inside_frame, width=20, font= "comicsans 11 bold", state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)
        
        #BUTTON FRAME
        btn_frame= Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=400, width=635, height=340)

        import_btn= Button(btn_frame, text="Import CSV", width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn= Button(btn_frame, text="Export CSV", width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1) 

        update_btn= Button(btn_frame, text="Update", width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2) 

        reset_btn= Button(btn_frame, text="Reset", width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3) 

        #RIGHT FRAME
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font = ("georgia", 14, "bold"))
        Right_frame.place(x=660, y=10, width=645, height=645)

        table_frame= Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=630, height=600)

        #========================scroll bar table======================================================================================

        scroll_x= ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("attendanceId", "Id", "Name", "Program", "Date", "Time", "Attendance"), xscrollcommand= scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side= BOTTOM, fill=X)
        scroll_y.pack(side= RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("attendanceId", text="Attendance ID")
        self.AttendanceReportTable.heading("Id", text="ID")
        self.AttendanceReportTable.heading("Name", text="Name")
        self.AttendanceReportTable.heading("Program", text="Program")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Attendance", text="Attendance Status")

        self.AttendanceReportTable["show"]= "headings"
        self.AttendanceReportTable.column("attendanceId", width=100)
        self.AttendanceReportTable.column("Id", width=100)
        self.AttendanceReportTable.column("Name", width=100)
        self.AttendanceReportTable.column("Program", width=100)
        self.AttendanceReportTable.column("Date", width=100)
        self.AttendanceReportTable.column("Time", width=100)
        self.AttendanceReportTable.column("Attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)












if __name__ == "__main__":
    root=Tk()
    obj= Attendance(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog, messagebox
from dotenv import load_dotenv
load_dotenv()

mydata=[]
class Attendance:
    def __init__(self, root):
            self.root=root
            self.root.geometry("1530x790+0+0")
            self.root.title("Face Recognition System")

            #==============================variable=====================================
            self.var_sno= StringVar()  
            self.var_std_id= StringVar()  
            self.var_atten_name= StringVar()  
            self.var_atten_program= StringVar()  
            self.var_atten_school= StringVar()  
            self.var_atten_time= StringVar()  
            self.var_atten_date= StringVar()  
            self.var_atten_attendance= StringVar() 

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
            # S.No.
            SNO_label = Label(left_inside_frame, text="S.No:", font=("georgia", 12, "bold"), bg="white")
            SNO_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

            SNO_entry = ttk.Entry(left_inside_frame, width=14, textvariable=self.var_sno, font=("georgia", 12))
            SNO_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

            # Student ID
            IdLabel = Label(left_inside_frame, text="Id:", font=("georgia", 12, "bold"), bg="white")
            IdLabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)

            Id_entry = ttk.Entry(left_inside_frame, width=14, textvariable=self.var_std_id, font=("georgia", 12))
            Id_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

            # Name
            nameLabel = Label(left_inside_frame, text="Name:", font=("georgia", 12, "bold"), bg="white")
            nameLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

            name_entry = ttk.Entry(left_inside_frame, width=14, textvariable=self.var_atten_name, font=("georgia", 12))
            name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

            # Program
            programLabel = Label(left_inside_frame, text="Program:", font=("georgia", 12, "bold"), bg="white")
            programLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)

            program_entry = ttk.Entry(left_inside_frame, width=14, textvariable=self.var_atten_program, font=("georgia", 12))
            program_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

            # School
            schoolLabel = Label(left_inside_frame, text="School:", font=("georgia", 12, "bold"), bg="white")
            schoolLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)

            school_entry = ttk.Entry(left_inside_frame, width=14, textvariable=self.var_atten_school, font=("georgia", 12))
            school_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

            # Time
            timeLabel = Label(left_inside_frame, text="Time:", font=("georgia", 12, "bold"), bg="white")
            timeLabel.grid(row=2, column=2, padx=10, pady=5, sticky=W)

            time_entry = ttk.Entry(left_inside_frame, width=14, textvariable=self.var_atten_time, font=("georgia", 12))
            time_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

            # Date
            dateLabel = Label(left_inside_frame, text="Date:", font=("georgia", 12, "bold"), bg="white")
            dateLabel.grid(row=3, column=2, padx=10, pady=5, sticky=W)

            date_entry = ttk.Entry(left_inside_frame, width=14, textvariable=self.var_atten_date, font=("georgia", 12))
            date_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

            # Attendance Status
            attendanceLabel = Label(left_inside_frame, text="Attendance Status:", font=("georgia", 12, "bold"), bg="white")
            attendanceLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)

            attendance_combo = ttk.Combobox(left_inside_frame, width=12, textvariable=self.var_atten_attendance, font=("georgia", 12), state="readonly")
            attendance_combo["values"] = ("Status", "Present", "Absent" )
            attendance_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)
            attendance_combo.set("Status")

            #BUTTON FRAME
            btn_frame= Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
            btn_frame.place(x=0, y=400, width=635, height=340)

            import_btn= Button(btn_frame, text="Import CSV", command=self.importCsv, width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
            import_btn.grid(row=0, column=0)

            export_btn= Button(btn_frame, text="Export CSV", command=self.exportCsv, width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
            export_btn.grid(row=0, column=1) 

            update_btn= Button(btn_frame, text="Update", command=self.update_data, width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
            update_btn.grid(row=0, column=2) 

            reset_btn= Button(btn_frame, text="Reset", width=15, command= self.reset_data, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
            reset_btn.grid(row=0, column=3) 

            #RIGHT FRAME
            Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font = ("georgia", 14, "bold"))
            Right_frame.place(x=660, y=10, width=645, height=645)

            table_frame= Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
            table_frame.place(x=5, y=5, width=630, height=600)
            
            #========================scroll bar table======================================================================================
            scroll_x= ttk.Scrollbar(table_frame, orient=HORIZONTAL)
            scroll_y= ttk.Scrollbar(table_frame, orient=VERTICAL)
            self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("S.No", "Id", "Name", "Program", "School", "Time", "Date", "Attendance"), xscrollcommand= scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.pack(side= BOTTOM, fill=X)
            scroll_y.pack(side= RIGHT, fill=Y)

            scroll_x.config(command=self.AttendanceReportTable.xview)
            scroll_y.config(command=self.AttendanceReportTable.yview)

            self.AttendanceReportTable.heading("S.No", text="S.No")
            self.AttendanceReportTable.heading("Id", text="ID")
            self.AttendanceReportTable.heading("Name", text="Name")
            self.AttendanceReportTable.heading("Program", text="Program")
            self.AttendanceReportTable.heading("School", text="School")
            self.AttendanceReportTable.heading("Time", text="Time")
            self.AttendanceReportTable.heading("Date", text="Date")
            self.AttendanceReportTable.heading("Attendance", text="Attendance Status")

            self.AttendanceReportTable["show"]= "headings"
            self.AttendanceReportTable.column("S.No", width=50)
            self.AttendanceReportTable.column("Id", width=100)
            self.AttendanceReportTable.column("Name", width=100)
            self.AttendanceReportTable.column("Program", width=100)
            self.AttendanceReportTable.column("School", width=100)
            self.AttendanceReportTable.column("Time", width=100)
            self.AttendanceReportTable.column("Date", width=100)
            self.AttendanceReportTable.column("Attendance", width=100)

            self.AttendanceReportTable.pack(fill=BOTH, expand=1)

            self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    #================fetch data===========================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for index, row in enumerate(rows, start=1):  # Start serial numbers from 1
            row_with_serial = (index, *row)
        self.AttendanceReportTable.insert("", END, values=row_with_serial)
    
    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        file = filedialog.askopenfilename(
            initialdir=os.getcwd(), title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*"))
        )
        if not file:
            return
        with open(file) as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            mydata = [row for row in csvreader]
        self.fetchData(mydata)
        
    # Export CSV
    def exportCsv(self):
        if not mydata:
            messagebox.showerror("Error", "No data to export")
            return
        file = filedialog.asksaveasfilename(
            initialdir=os.getcwd(), title="Save CSV",
            defaultextension=".csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*"))
        )
        if not file:
            return
        with open(file, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["S.No", "ID", "Name", "Program", "School", "Time", "Date", "Attendance"])
            for index, row in enumerate(mydata, start=1):
                writer.writerow((index, *row))
        messagebox.showinfo("Export", f"Data exported to {file}")
    
    def get_cursor(self, event=""):
        try:
            # Get the selected row
            cursor_row = self.AttendanceReportTable.focus()
            content = self.AttendanceReportTable.item(cursor_row)
            rows = content['values']

            if not rows:
                # Handle empty row selection
                messagebox.showerror("Error", "No valid record selected", parent=self.root)
                return

            # Set the retrieved values to the respective variables
            self.var_sno.set(rows[0])
            self.var_std_id.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_program.set(rows[3])
            self.var_atten_school.set(rows[4])
            self.var_atten_time.set(rows[5])
            self.var_atten_date.set(rows[6])
            self.var_atten_attendance.set(rows[7])

        except IndexError as e:
            # Handle index errors if rows do not contain the expected number of elements
            messagebox.showerror("Error", f"Unexpected row format: {e}", parent=self.root)
        except Exception as e:
            # Handle any other unexpected errors
            messagebox.showerror("Error", f"An error occurred: {e}", parent=self.root)

    
    def reset_data(self):
        self.var_sno.set("")
        self.var_std_id.set("")
        self.var_atten_name.set("")
        self.var_atten_program.set("")
        self.var_atten_school.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
    
    #update function

    def update_data(self):
        try:
            selected_item = self.AttendanceReportTable.selection()  # Get the selected row
            if not selected_item:
                messagebox.showerror("Error", "No record selected to update", parent=self.root)
                return

            # Get the current row data from the selection
            selected = self.AttendanceReportTable.item(selected_item)
            values = selected['values']

            if not values:
                messagebox.showerror("Error", "No valid data selected to update", parent=self.root)
                return

            # Collect updated values from the form fields
            updated_values = (
                self.var_sno.get(),
                self.var_std_id.get(),
                self.var_atten_name.get(),
                self.var_atten_program.get(),
                self.var_atten_school.get(),
                self.var_atten_time.get(),
                self.var_atten_date.get(),
                self.var_atten_attendance.get()
            )

            # Ensure no field is empty
            if "" in updated_values or updated_values[7] == "Status":
                messagebox.showerror("Error", "All fields are required, including a valid attendance status.", parent=self.root)
                return

            # Update the selected row in Treeview
            self.AttendanceReportTable.item(selected_item, values=updated_values)

            # Update the corresponding entry in `mydata`
            row_index = int(values[0]) - 1  # S.No is 1-based; adjust for 0-based index
            if 0 <= row_index < len(mydata):
                mydata[row_index] = updated_values[1:]  # Exclude S.No for `mydata`

            messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while updating the data: {e}", parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj= Attendance(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #========variables=========#
        self.var_school= StringVar()
        self.var_course=StringVar()
        self.var_program=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_gpa=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_hosteler=StringVar()
        self.var_proctor=StringVar()

        #bg img
        img = Image.open(r"D:\Face_Recognition_System\Face-Recognition-Student-Attendance-System\Project imgs\bgimg.png")
        img = img.resize((1530,790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image = self.photoimg)
        bg_img.place(x = 0, y= 0, width = 1400, height = 790)
        
        title_lbl = Label(bg_img, text = "STUDENT MANAGEMENT SYSTEM", font=("georgia", 35,"bold"), bg= "black", fg="white")
        title_lbl.place(x=0, y=0, width= 1400, height= 45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1320, height=670)
 
        #LEFT LABEL FRAME
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font = ("georgia", 14, "bold"))
        Left_frame.place(x=10, y=10, width=640, height=645)

        img_left = Image.open(r"C:\Users\Dell\OneDrive\Desktop\Face_recognition_system\Project imgs\std_details_icon.png")
        img_left = img_left.resize((632,140), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        bg_img = Label(Left_frame, image = self.photoimg_left)
        bg_img.place(x=1, y=0, width= 634, height= 130)

        #current course
        current_course_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Current course", font = ("georgia", 14, "bold"))
        current_course_frame.place(x=14, y=160, width= 632, height= 150)
        
        #school
        school_label= Label(current_course_frame, text="School", font=("georgia", 12, "bold"), bg="white")
        school_label.grid(row=0, column=0, padx=1,  sticky=W)

        school_combo= ttk.Combobox(current_course_frame,textvariable= self.var_school,font=("georgia", 12, "bold"), state="read only")
        school_combo["values"]=("Select School", "SCSE", "SASL", "SEEE", "SMEC", "SBET", "School of Architecture","BS")
        school_combo.current(0)
        school_combo.grid(row=0, column=1, padx=1, pady=10, sticky=W) 
        
        #program label
        pgrm_label= Label(current_course_frame, text="Program", font=("georgia", 12, "bold"), bg= "white")
        pgrm_label.grid(row=0, column=2, padx=10, sticky=W)

        pgrm_combo= ttk.Combobox(current_course_frame, textvariable=self.var_program,font=("georgia", 12, "bold"), state="read only")
        pgrm_combo["values"]=("Select Program", "BTech", "Mtech", "Int. MTech", "B.Arch", "BBA")
        pgrm_combo.current(0)
        pgrm_combo.grid(row=0, column=3, padx=0, pady=10, sticky=W)

        #Course
        course_label= Label(current_course_frame, text="Course", font=("georgia", 12, "bold"), bg="white")
        course_label.grid(row=1, column=0, padx=1, sticky= W)

        course_combo= ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("georgia", 12, "bold"), state="read only")
        course_combo["values"]=("Select Course", "CSE", "CSE-AIML", "Cyber Security and Digital Forensics", "Gaming Technology")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=1, pady=10, sticky=W) 
        
        #Year
        year_label= Label(current_course_frame, text="Year", font=("georgia", 12, "bold"), bg="white")
        year_label.grid(row=1, column=2, padx=10, sticky=W)

        year_combo= ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("georgia", 12, "bold"), state="read only")
        year_combo["values"]=("Select Year", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=0, pady=10, sticky=W)
        
        #Semester
        sem_label= Label(current_course_frame, text="Semester", font=("georgia", 12, "bold"), bg="white")
        sem_label.grid(row=2, column=0, padx=1, sticky=W)

        sem_combo= ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("georgia", 12, "bold"), state="read only")
        sem_combo["values"]=("Select Semester", "Summer 2022-23", "Fall 2022-23", "Winter 2022-23", "Summer 2023-24", "Fall 2023-24", "Winter 2023-24")
        sem_combo.current(0)
        sem_combo.grid(row=2, column=1, padx=2, pady=8, sticky=W)

        #================================================================================================================================#
        
        # Personal Info Frame
        class_student_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Personal Information", font=("georgia", 14, "bold"))
        class_student_frame.place(x=14, y=320, width=632, height=345)

        # Student ID
        studentId_label = Label(class_student_frame, text="Student ID:", font=("georgia", 12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=14, font=("georgia", 12))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("georgia", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=14, font=("georgia", 12))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Gender
        Gender_label = Label(class_student_frame, text="Gender:", font=("georgia", 12, "bold"), bg="white")
        Gender_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, width=14, textvariable=self.var_gender, font=("georgia", 12), state="readonly")
        gender_combo["values"] = ("Select", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # DOB
        DOB_label = Label(class_student_frame, text="DOB:", font=("georgia", 12, "bold"), bg="white")
        DOB_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        DOB_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=14, font=("georgia", 12))
        DOB_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # GPA
        GPA_label = Label(class_student_frame, text="GPA:", font=("georgia", 12, "bold"), bg="white")
        GPA_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        GPA_entry = ttk.Entry(class_student_frame, textvariable=self.var_gpa, width=14, font=("georgia", 12))
        GPA_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Email
        Email_label = Label(class_student_frame, text="Email:", font=("georgia", 12, "bold"), bg="white")
        Email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=14, font=("georgia", 12))
        Email_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Phone
        Phone_label = Label(class_student_frame, text="Phone:", font=("georgia", 12, "bold"), bg="white")
        Phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=14, font=("georgia", 12))
        Phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Proctor
        Proctor_label = Label(class_student_frame, text="Proctor:", font=("georgia", 12, "bold"), bg="white")
        Proctor_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Proctor_entry = ttk.Entry(class_student_frame, textvariable=self.var_proctor, width=14, font=("georgia", 12))
        Proctor_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        #Address
        Address_label= Label(class_student_frame, text="Address:", font=("georgia", 12, "bold"), bg="white")
        Address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        Address_entry=ttk.Entry(class_student_frame, textvariable=self.var_address, width=14, font=("georgia", 12))
        Address_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        #Hosteler
        Hosteler_label= Label(class_student_frame, text="Hosteler:", font=("georgia", 12, "bold"), bg="white")
        Hosteler_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Hosteler_entry=ttk.Entry(class_student_frame, textvariable=self.var_hosteler, width=14, font=("georgia", 12))
        Hosteler_entry.grid(row=4, column=1, padx=2, pady=5, sticky=W)
        
        #RADIO BUTTONS
        style = ttk.Style()
        style.configure("Custom.TRadiobutton", font=("Georgia", 12), bg="white", foreground="black")
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)
        
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        #BUTTON FRAMES 
        btn_frame= Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=220, width=635, height=40)

        save_btn= Button(btn_frame, text="Save", command=self.add_data, width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn= Button(btn_frame, text="Update", width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1) 

        delete_btn= Button(btn_frame, text="Delete", width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2) 

        reset_btn= Button(btn_frame, text="Reset", width=15, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3) 

        btn_frame1= Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=257, width=635, height=40)

        Take_photo_btn= Button(btn_frame1, text="Take Photo", width=32, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        Take_photo_btn.grid(row=1, column=0)

        Update_photo_btn= Button(btn_frame1, text="Update Photo", width=32, font=("Geoegia", 12, "bold"), bg="blue", fg="white")
        Update_photo_btn.grid(row=1, column=1)


        ##==============================================================================================================================================================##
        #RIGHT LABEL FRAME

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font = ("georgia", 14, "bold"))
        Right_frame.place(x=660, y=10, width=645, height=640)

        img_right = Image.open(r"C:\Users\Dell\OneDrive\Desktop\Face_recognition_system\Project imgs\std_details_icon.png")
        img_right = img_right.resize((634,140), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        bg_img1 = Label(Right_frame, image = self.photoimg_right)
        bg_img1.place(x=3, y=0, width=634, height=125)

        #SEARCH FRAME

        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System ", font = ("georgia", 14, "bold"))
        Search_frame.place(x=2, y=130, width=635, height=75)
        
        Search_label = Label(Search_frame, text="Search By:", font=("georgia", 12, "bold"), bg="white")
        Search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        Search_combo= ttk.Combobox(Search_frame, font=("georgia", 12), state="read only", width=12)
        Search_combo["values"]=("Select", "Student ID", "Student Name", "Phone No", "DOB")
        Search_combo.current(0)
        Search_combo.grid(row=0, column=1, padx=2, pady=8, sticky=W)

        Search_entry= ttk.Entry(Search_frame, width=12, font=("georgia", 12))
        Search_entry.grid(row=0, column=2, padx=5, pady= 5, sticky=W)

        Search_btn=Button(Search_frame,text="Search", width=10, font=("Georgia", 12, "bold"), bg="blue", fg="white")
        Search_btn.grid(row=0, column=3, padx= 1)

        ShowAll_btn=Button(Search_frame, text="Show All", width=10, font=("Georgia", 12, "bold"), bg="blue", fg="white")
        ShowAll_btn.grid(row=0, column=4, padx= 1)
        
        #TABLE FRAME
        
        Table_frame = Frame(Right_frame, bd=2, bg="white", relief= RIDGE)
        Table_frame.place(x=2, y=207, width= 635, height= 400)

        scroll_x= ttk.Scrollbar(Table_frame, orient=HORIZONTAL)       
        scroll_y= ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.student_table= ttk.Treeview(Table_frame, column=("Student ID", "Name", "Gender", "DOB", "School", "Program", "Course", "Year", "Semester", "GPA", "Email", "Phone No", "Address", "Hosteler", "Proctor", "Photo"))
        scroll_x.pack(side= BOTTOM, fill=X)
        scroll_y.pack(side= RIGHT, fill=Y)
        scroll_x.config(command= self.student_table.xview)
        scroll_y.config(command= self.student_table.yview)

        self.student_table.heading("Student ID", text="Student ID")
        self.student_table.heading("Name", text="Student Name")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("School", text="School")
        self.student_table.heading("Program", text="Program")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester") 
        self.student_table.heading("GPA", text="GPA")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone No", text="Pone No")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Hosteler", text="Hosteler")
        self.student_table.heading("Proctor", text="Proctor")
        self.student_table.heading("Photo", text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("Student ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("School", width=100)
        self.student_table.column("Program", width=100)
        self.student_table.column("Course" ,width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("GPA", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Hosteler",width=100)
        self.student_table.column("Proctor", width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

#=====================get cursor==========================#
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content['values']
        
        if data:  # Check if data is available
            self.var_std_id.set(data[0])
            self.var_std_name.set(data[1])
            self.var_gender.set(data[2])
            self.var_dob.set(data[3])
            self.var_school.set(data[4])
            self.var_program.set(data[5])
            self.var_course.set(data[6])
            self.var_year.set(data[7])
            self.var_semester.set(data[8])
            self.var_gpa.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_hosteler.set(data[13])
            self.var_proctor.set(data[14])
            self.var_radio1.set(data[15])

        self.fetch_data()   # No need to call fetch_data() inside the get_cursor method

#  =====================function declaration===============================#

    def add_data(self):
        if self.var_school.get()=="Select School" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All fields are required!", parent= self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Bareera@21",database="face recognition" )
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_school.get(),
                                                                                                        self.var_program.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_gpa.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_hosteler.get(),
                                                                                                        self.var_proctor.get(),
                                                                                                        self.var_radio1.get()

                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    


#==========================fetch data=======================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Bareera@21",database="face recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

# update function
    def update_data(self):
        if self.var_school.get()=="Select School" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent= self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Bareera@21",database="face recognition" )
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Std_id=%s,Std_name=%s,Gender=%s,DOB=%s,School=%s,Program=%s,Course=%s,Year=%s,Semester=%s,GPA=%s,Email=%s,Phone=%s,Address=%s,Hosteler=%s,Proctor=%s,Photo=%s where Student_id=%s",(
                                                                                                        
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_school.get(),
                                                                                                        self.var_program.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_gpa.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_hosteler.get(),
                                                                                                        self.var_proctor.get(),
                                                                                                        self.var_radio1.get()
                                                                                                    ))    
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    # delete function
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student ID is required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Bareera@21",database="student")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)           

    #reset
    def reset_data(self):
            self.var_school.set("Select School")
            self.var_course.set("Select Course")
            self.var_program.set("Select Program")
            self.var_year.set("Select Year")
            self.var_semester.set("Select Semester")
            self.var_std_id.set("")
            self.var_std_name.set("")
            self.var_gpa.set("")
            self.var_gender.set("Select Gender")
            self.var_dob.set("")
            self.var_email.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_hosteler.set("")
            self.var_proctor.set("")
            self.var_radio1.set("")

    def generate_dataset(self):
        if self.var_school.get()=="Select School" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent= self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Bareera@21",database="student" )
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresults:
                    id+=1
                my_cursor.execute("update student set Std_id=%s,Std_name=%s,Gender=%s,DOB=%s,School=%s,Program=%s,Course=%s,Year=%s,Semester=%s,GPA=%s,Email=%s,Phone=%s,Address=%s,Hosteller=%s,Proctor=%s,Photo=%s where Student_id=%s",(
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_school.get(),
                                                                                                                                                                                                                self.var_program.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_gpa.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_hosteler.get(),
                                                                                                                                                                                                                self.var_proctor.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_std_id.get()  
                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()  
                conn.close()
            except mysql.connector.Error as error:
                print(f"Error: {error}")

                                                                                

if __name__ == "__main__":
    root=Tk()
    obj= Student(root)
    root.mainloop()
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import Image
import face_recognition
import cv2
import numpy as np
import os
import pandas as pd


def addImage(path,name,new_window):
    image = face_recognition.load_image_file(path)
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

    for face_location in face_locations:

        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save("C://Users//abhishek kushwaha//Desktop//mark attendance//traningData//data"+"//"+name+".jpg")
    messagebox.showinfo("Success", "Successfully added the image in Database")
    new_window.destroy()

def generateExcelSheet(date,pathOfGroupImage,pathOfExcelFile,new_window):
    known_face_encodings = []
    known_face_names = []

    excel_file = pd.read_excel(pathOfExcelFile)


    path = "./traningData/data"
    traning_data = os.listdir(path)

    for img in traning_data:
        image = face_recognition.load_image_file(path+"//"+img)
        face_encoding = face_recognition.face_encodings(image)[0]
        face_name = img[:-4]
        known_face_encodings.append(face_encoding)
        known_face_names.append(face_name)

    unknown_image = face_recognition.load_image_file(pathOfGroupImage)

    unknown_face_encoding = face_recognition.face_encodings(unknown_image)

    face_names = []
    for face_encoding in unknown_face_encoding:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            face_names.append(known_face_names[best_match_index])

    excel_file = pd.read_excel(pathOfExcelFile)
    l = []
    for i in excel_file.Name:
        if i in face_names:
            l.append("P")
        else:
            l.append("A")
    print(face_names)
    
    excel_file[date] = l
    path = "C://Users//abhishek kushwaha//Desktop"
    excel_file.to_excel(path+"//student"+date+".xlsx",index=False)
    messagebox.showinfo("Success", "Successfully Generated the Excel Sheet")
    new_window.destroy()


def openNewWindow():
    def browsefunc():
        ent1.insert(0, "")
        filename =askopenfilename(filetypes=(("jpag files","*.jpg"),("All files","*.*")))
        ent1.insert(END,filename)
    new_window = Toplevel(root)
    new_window.geometry("1050x750")

    new_window.title("Add Student")
    new_window.configure(bg="black")
    new_window.resizable(False,False)
    l1 = Label(new_window, text = "Add new Student Details", width = 45, font =("italic",25,"bold"), bg = 'orange')
    l1.place(x=70, y=50)


    path = StringVar()
    name = StringVar()
    l2 = Label(new_window, text = "Student Name", width = 16, font =("italic",15,"bold"), bg = 'blue',fg='white')
    l2.place(x=260, y=250)
    ent1=Entry(new_window,font=42,width = 31,textvariable=name)
    ent1.place(x=480,y=250,height=30)
    l3 = Label(new_window, text = "Image Path", width = 16, font =("italic",15,"bold"), bg = 'blue',fg='white')
    l3.place(x=260, y=300)
    ent1=Entry(new_window,font=42,width=25,textvariable=path)
    ent1.place(x=480,y=300,height=30)
    b1=Button(new_window,text="Browse",bg="white",fg="black",font=("Times",12,"bold"),command=browsefunc)
    b1.place(x=760,y=300)
    btn = Button(new_window,text="Add Student",bg="blue",fg="white",font=("Times",15,"bold"),command= lambda: addImage(path.get(),name.get(),new_window))
    btn.place(x=450,y=400,width=250,height=45)



def openNewWindow2():
    def browsefunc1():
        ent1.insert(0, "")
        filename =askopenfilename(filetypes=(("jpag files","*.jpg"),("All files","*.*")))
        ent1.insert(END,filename)
    def browsefunc2():
        ent2.insert(0, "")
        filename1 =askopenfilename(filetypes=(("Excel files","*.xlsx"),("All files","*.*")))
        ent2.insert(END,filename1)
    new_window = Toplevel(root)
    new_window.geometry("1050x750")
    new_window.title("Mark attendace")
    new_window.configure(bg="black")
    new_window.resizable(False,False)
    pathOfGroupImg = StringVar()
    pathOfExcelFile = StringVar()
    date = StringVar()
    lp1 = Label(new_window, text = "Generate Attendance Excel Sheet", width = 45, font =("italic",25,"bold"), bg = 'orange')
    lp1.place(x=70, y=50)
    l2 = Label(new_window, text = "Enter Date", width = 16, font =("italic",15,"bold"), bg = 'blue',fg='white')
    l2.place(x=260, y=250)
    ent1=Entry(new_window,font=42,width = 31,textvariable=date)
    ent1.place(x=480,y=250,height=30)
    l3 = Label(new_window, text = "Image Path", width = 16, font =("italic",15,"bold"), bg = 'blue',fg='white')
    l3.place(x=260, y=300)
    ent1=Entry(new_window,font=42,width=25,textvariable=pathOfGroupImg)
    ent1.place(x=480,y=300,height=30)
    b1=Button(new_window,text="Browse",bg="white",fg="black",font=("Times",12,"bold"),command=browsefunc1)
    b1.place(x=760,y=300)
    l4 = Label(new_window, text = "Excelsheet Path", width = 16, font =("italic",15,"bold"), bg = 'blue',fg='white')
    l4.place(x=260, y=350)
    ent2=Entry(new_window,font=42,width=25,textvariable=pathOfExcelFile)
    ent2.place(x=480,y=350,height=30)
    b2=Button(new_window,text="Browse",bg="white",fg="black",font=("Times",12,"bold"),command=browsefunc2)
    b2.place(x=760,y=350)
    
    btn = Button(new_window,text="Generate Excel Sheet",bg='blue',fg='white',font=('Times',15,'bold'),command=lambda: generateExcelSheet(date.get(),pathOfGroupImg.get(),pathOfExcelFile.get(),new_window))
    btn.place(x=450,y=450,width=250,height=45)





root = Tk()
lebel_home = Label()

levelhome = Label(root, text = "Automated Attendance Marking System", width = 45, font =("italic",25,"bold"), bg = 'orange')
levelhome.place(x=70, y=50)


btn = Button(root,text="Add New Student ", bg="blue", fg ="white", font=("times",15,"bold"),command=openNewWindow)
btn.place(x=290, y=330)

btn1 = Button(root,text="Mark Attendace",bg="blue", fg ="white", font=("times",15,"bold"),command= openNewWindow2)
btn1.place(x=610, y=330)
root.geometry("1050x750")
root.title("Mark attendace Automatically")
root.configure(bg="black")
root.mainloop()
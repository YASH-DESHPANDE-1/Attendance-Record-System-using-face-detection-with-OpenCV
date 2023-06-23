import face_recognition
import cv2
import numpy as np
import csv
import os
from tkinter import *
import tkinter as tk
from datetime import datetime

def show_text():
    
    video_capture = cv2.VideoCapture(0)
 
    amitabh_bacchan_image = face_recognition.load_image_file("photos/amitji.jpg")
    amitabh_bacchan_encoding = face_recognition.face_encodings(amitabh_bacchan_image)[0]
 
    snoop_dogg_image = face_recognition.load_image_file("photos/snoop.jpg")
    snoop_dogg_encoding = face_recognition.face_encodings(snoop_dogg_image)[0]

    rahul_image = face_recognition.load_image_file("photos/rahul.jpg")
    rahul_encoding = face_recognition.face_encodings(rahul_image)[0]
 
 
 
    known_face_encoding = [
    amitabh_bacchan_encoding,
    snoop_dogg_encoding,
    rahul_encoding,
    #tesla_encoding
    ]
 
    known_faces_names = [
    "amitji - 33",
    "snoop - 69",
    "rahul - 82"
    ]
 
    students = known_faces_names.copy()
 
    face_locations = []
    face_encodings = []
    face_names = []
    s=True

 
 
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
 
 
 
    f = open(current_date+'.csv','w+',newline = '')
    lnwriter = csv.writer(f)
 
    while True:
        _,frame = video_capture.read()
        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgb_small_frame = small_frame[:,:,::-1]
        if s:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                name=""
                face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]
 
                face_names.append(name)
                if name in known_faces_names:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    bottomLeftCornerOfText = (10,100)
                    fontScale              = 1.5
                    fontColor              = (255,0,0)
                    thickness              = 3
                    lineType               = 2
 
                    cv2.putText(frame,name+' Present', 
                        bottomLeftCornerOfText, 
                        font, 
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)
 
                    if name in students:
                        students.remove(name)
                        print(students)
                        current_time = now.strftime("%H-%M-%S")
                        lnwriter.writerow([name,current_time])
        cv2.imshow("attendence system",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()

root=Tk()
root.geometry('400x400')
#c=Canvas(root,bg="gray16", height=200, width=200)
#image=ImageTK.PhotoImage(Image.open("bg\dypu.jpg"))
#c.create_image(0, 0, anchor-NW, image=image)
#c.pack()
#filename=PhotoImage(file="bg\dypu.jpg")
#background_label=Label(root, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#c.pack()
root.title("Attendance System DYPU")
root.configure(background='lightgreen')
mylabel = tk.Label(root, text="Attendance System", background="grey", font="45")
mylabel.pack()
mylabel2 = tk.Label(root, text="", pady=60, background="lightgreen")
mylabel2.pack()
button=Button(root, text="Start Attendance", background="powderblue", padx=50, pady=20, command=show_text)
button.pack()
root.mainloop()


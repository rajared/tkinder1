# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
import tkinter.messagebox



def button_click():
    text_box_infunction=text_data1.get()
    file=open("employe.xlsx",'a')
    file.write(text_box_infunction)
    file.close()
    tkinter.messagebox.showinfo("1st click",text_box_infunction)

window=tkinter.Tk()
window.title("welcome")
window.geometry('300x300')
frame1=Frame(window)
frame1.pack()
frame2=Frame(window)
frame2.pack(side=BOTTOM)
text_data = StringVar()
text_data1 = StringVar()
lable1=Label(frame1,textvar=text_data)
text_data.set('name')
lable1.pack()
text_box=Entry(frame1,textvar=text_data1)
text_box.pack()
text_button=Button(frame2,text='submit',command=button_click)
text_button.pack()
window.mainloop()




# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

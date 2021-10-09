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
text_data = StringVar()
text_data1 = StringVar()
lable1=Label(window,textvar=text_data)
text_data.set('name')
lable1.grid(row=0,column=0)
text_box=Entry(window,textvar=text_data1)
text_box.grid(row=0,column=1)
text_button=Button(window,text='submit',command=button_click)
text_button.grid(row=1,column=1)
window.mainloop()




# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

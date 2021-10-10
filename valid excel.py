# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
import tkinter.messagebox
from os.path import exists
import pandas
from openpyxl import *
import xlsxwriter

def validate_psn():
    if box_psn.get()<10:
        return True
    else:
        return False


window=tkinter.Tk()
window.title("Registration")
window.geometry('600x600')
text_data = StringVar()
text_name = StringVar()
lable1=Label(window,textvar=text_data)
text_data.set('name')
lable1.grid(row=0,column=5)

text_ema = StringVar()
lemail=Label(window,textvar=text_ema)
text_ema.set('email')
lemail.grid(row=1,column=5)
box_ema=StringVar()
box_ema=Entry(window,textvar=box_ema)
box_ema.grid(row=1,column=6)

text_psn = StringVar()
lpsno=Label(window,textvar=text_psn)
text_psn.set('psnumber')
lpsno.grid(row=2,column=5)
box_psn=int()
box_psn=Entry(window,textvar=box_psn,validate="focusout", validatecommand=validate_psn)
box_psn.grid(row=2,column=6)



text_loc = StringVar()
lloc=Label(window,textvar=text_loc)
text_loc.set('location')
lloc.grid(row=3,column=5)
box_loc=StringVar()
box_loc=Entry(window,textvar=box_loc)
box_loc.grid(row=3,column=6)


def viewSelected():
    choice = var.get()
    if choice == 1:
        output = "IT"
    elif choice == 2:
        output = "HR"
    else:
        output = "Invalid selection"
    return tkinter.messagebox.showinfo('PythonGuides', f'You Selected {output}.')


var = IntVar()
Radiobutton(window, text="IT", variable=var, value=1, command=viewSelected).grid(row=4,column=6)
Radiobutton(window, text="HR", variable=var, value=2, command=viewSelected).grid(row=4,column=7)
text_req = StringVar()
lreq=Label(window,textvar=text_req)
text_req.set('request')
lreq.grid(row=4,column=5)


text_des = StringVar()
ldes=Label(window,textvar=text_des)
text_des.set('description')
ldes.grid(row=5,column=5)
box_des=StringVar()
box_des=Entry(window,textvar=box_des)
box_des.grid(row=5,column=6)


text_box=Entry(window, textvar=text_name)
text_box.grid(row=0,column=6)

text_box_infunction1 = {}
request1 = StringVar()


def error():
    tkinter.messagebox.showinfo('give valid data')
def button_click():
    text_box_infunction1={ 'name':[text_name.get()],
                          'psno' :[box_psn.get()],
                          'email':[box_ema.get()],
                          'request':[var.get()],
                           'location':[box_loc.get()],
                          'discriptiion':[box_des.get()]
                           }
    tkinter.messagebox.showinfo("1st click",text_box_infunction1)
    df=pandas.DataFrame(text_box_infunction1)
    print(df)
    df.to_excel('employe.xlsx')
text_button=Button(window,text='submit',command=button_click)
text_button.grid(row=9,column=6)

window.mainloop()




# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

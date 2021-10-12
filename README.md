# tkinder1
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
import tkinter.messagebox

import pandas as pd
from pandas import *
from os.path import exists
global list_name,list_psno,list_email

def button_click():
    validinputs=[validate_psn(),validate_loc()
                 ,validate_ema(),validate_des()
                 ,validate_nam()]

    if False not in validinputs:
        if var.get()==1:
            request='IT'
        else:
            request='HR'
        box_psn2=int(box_psn.get())
        text_box_infunction1={ 'name':[box_name.get()],
                          'psno' :[box_psn2],
                          'email':[box_ema.get()],
                          'request':[request],
                           'location':[box_loc.get()],
                          'discriptiion':[box_des.get()]
                           }
        tkinter.messagebox.showinfo("1st click",text_box_infunction1)
        if exists('ltts.xlsx')==True:
            df = pd.read_excel('ltts.xlsx')
            global list_name,list_psno,list_email,psno
            list_name=df['name'].to_list()
            list_psno=df['psno'].to_list()
            list_email=df['email'].to_list()
            if box_name.get() in list_name:
                print('name not available plz give another name')
            elif box_psn2 in list_psno:
                print('psno already present ,please give another psno')
            elif box_ema.get() in list_email:
                print('email already prasent,plz provide another mailid')
            else:
                df1 = pd.DataFrame(text_box_infunction1)
                dff = df.append(df1, ignore_index=True)
                dff.drop(dff.columns[dff.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
                dff.to_excel('ltts.xlsx')
                print(dff)
                print("you have successfully registered")

        else:
            f=open('ltts.xlsx','x')
            f.close()
            df=pandas.DataFrame(text_box_infunction1)
            df.to_excel('ltts.xlsx')
            print(df)

def validate_nam():
    name=box_name.get()
    if name.isdigit():
        print('name should be charecters')
    elif len(str(box_name.get())) >3:
        return True
    else:
        print('name must be atlest 4 letters')
        return False

def validate_psn():
    if len((box_psn.get()))== 8:
        return True
    else:
        print('please enter 8 digits psn number or you mixed with string')
        return False

def validate_loc():
    locations=['hyderabad','banglore','mysore','mumbai']
    if box_loc.get() in locations:
        return True
    else:
        print('location must be an entry in the location list')
        return False
def validate_des():
    if box_des.get()!='':
        return True
    else:
        print('description must not be empty')
        return False
def validate_ema():
    str1=box_ema.get()
    str=box_ema.get().split('@')
    if ('.' in str[0]):
        if ('@ltts.com' in str1):
            return True
        else:
            print('it is not ltts mail plz give ltts mail')
            return False
    else:
        print('their must be a one dot in the befor @ in the ltts mail')
        return False



window=tkinter.Tk()
window.title("Registration")
window.geometry('600x600')
text_nam = StringVar()
box_name = StringVar(window,value='rajareddy')
lable1=Label(window,textvar=text_nam)
text_nam.set('name')
lable1.grid(row=0,column=5)

text_ema = StringVar()
lemail=Label(window,textvar=text_ema)
text_ema.set('email')
lemail.grid(row=1,column=5)
box_ema=StringVar(window,value='guttikondarajavardhan.reddy@ltts.com')
box_ema=Entry(window,textvar=box_ema,validate="focusout", validatecommand=validate_ema)
box_ema.grid(row=1,column=6)

text_psn = IntVar()
lpsno=Label(window,textvar=text_psn)
text_psn.set('psnumber')
lpsno.grid(row=2,column=5)
box_psn=IntVar(window,value='99005559')
box_psn=Entry(window,textvar=box_psn,validate="focusout", validatecommand=validate_psn)
box_psn.grid(row=2,column=6)



text_loc = StringVar()
lloc=Label(window,textvar=text_loc)
text_loc.set('location')
lloc.grid(row=3,column=5)
box_loc=StringVar(window,value='hyderabad')
box_loc=Entry(window,textvar=box_loc,validate="focusout", validatecommand=validate_loc)
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
box_des=StringVar(window,value='it')
box_des=Entry(window,textvar=box_des,validate="focusout", validatecommand=validate_des)
box_des.grid(row=5,column=6)


text_box=Entry(window, textvar=box_name,validate="focusout", validatecommand=validate_nam)
text_box.grid(row=0,column=6)
text_button=Button(window,text='submit',command=button_click)
text_button.grid(row=9,column=6)

window.mainloop()




# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

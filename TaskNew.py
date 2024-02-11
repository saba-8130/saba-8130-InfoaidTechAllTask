#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''To create To-Do List application using by GUI
    and commmand line application in python'''

#import GUI

import tkinter
from tkinter import*

root = Tk()

#width and height
root.geometry("400x650")

#Title for our program
root.title("To-Do-List")
root.resizable(False,False)

#task list
task_list=[]

def on_key_press(event):
    if field.get() != '':
        btn_text.set("SUBMIT")

#a funtion to get user enter input
def addTask():
    action_btn = btn_text.get()
    if action_btn == "SUBMIT":
        task = field.get()
        field.delete(0,END)

        if task:
            with open("tasklist.txt",'a') as taskfile:
                taskfile.write(f"\n{task}")
                task_list.append(task)
                listbox.insert(END,task)

    if action_btn == "SUBMIT":
        task = field.get()
        field.delete(0,END)

        if task:
            with open("tasklist.txt",'a') as taskfile:
                taskfile.write(f"\n{task}")
                task_list.append(task)
                listbox.insert(END,task)
            btn_text.set("SUBMIT")

def updateTask(event):
    selected_list_item = event.widget.get(event.widget.curselection()[0])
    entry_field_value.set(selected_list_item)
    

#a funtion to delete task
def deleteTask():
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)
        selected_list_item = ''
        entry_field_value.set(selected_list_item)
        btn_text.set("SUBMIT")
    
def openTaskFile():
    
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)

    except:
        file=open('tasklist.txt','w')
        file.close()

    
# Heading for our list

heading = Label(root,text="TO-DO LIST\n[ALL TASK] ", font="arial 20 bold", fg ="white",bg = "Green")
heading.pack(padx=100,pady=16)

#frame and entry space
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

entry_field_value= StringVar()
field = Entry(frame,width=18,font="arial 20",bd=0, textvariable=entry_field_value)
field.place(x=10,y=7)
field.focus()

#Button for adding  task .
btn_text = StringVar()
button = Button(frame, textvariable=btn_text,font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff",bd=0 ,command=addTask).place(x=300,y=0)
btn_text.set("SUBMIT")

#listbox.
f1=Frame(root,bd=3,width=700,height=200,bg="green")
f1.pack(pady=(160,0))

listbox = Listbox(f1,font=("arial",12),width=40,height=16,bg="green",cursor ="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH,padx=2)
scrollbar=Scrollbar(f1)
scrollbar.pack(side=RIGHT,fill=BOTH)


openTaskFile()


#delete option
Delete = Button(root,text="Delete",font="arial 18 bold",width=5, bg="#5a95ff",fg="#fff",bd=0 , command=deleteTask).pack()

#listbox.bind('<<ListboxSelect>>', updateTask)
listbox.bind('<Double-1>', updateTask)
field.bind('<KeyPress>', on_key_press) 

root.mainloop()


# In[ ]:





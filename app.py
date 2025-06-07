from tkinter import *
from tkinter import ttk
from datetime import datetime

root = Tk()
root.title("ToDo List")
root.geometry("800x560")
root['bg'] = '#333'


now = datetime.now()
dataTask = []

def getToDoData():
    title = titleInput.get()
    subtitle = subtitleInput.get()

    if title and subtitle:
        task = {"title": title, "subtitle": subtitle}
        dataTask.append(task)
        listBoxUpdate()


def listBoxUpdate():
    listToDoList.delete(0, END)


    for task in dataTask:
        data = f"{task['title']}    |    {task['subtitle']}    |    {now.strftime('%d.%m.%y %I:%M')}"
        listToDoList.insert(END, data)

    titleInput.delete(0, END)
    subtitleInput.delete(0, END)
    deleteBtn.pack_forget()


def deleteTask(event=None):
    selection = listToDoList.curselection()
    if selection or deleteBtn['text'] == 'Delete':
        index = selection[0]
        if 0 <= index < len(dataTask):
            dataTask.pop(index)
            listBoxUpdate() 



def deleteList(event):
    if listToDoList.curselection():
        deleteBtn.pack(anchor=NW,  expand=True, padx=15, pady=10)
    else:
        deleteBtn.pack_forget()



style = ttk.Style()
style.theme_use("clam")

style.configure("Green.TButton",
                background="#1bb547",
                foreground="#373837",
                font=("Arial", 15))


style.configure("Red.TButton",
                background="#f54263",
                foreground="#36040d",
                font=("Arial", 15))

style.configure("TLabel", 
                background="#333",
                foreground="white",
                font=("Arial", 14))
               

titleLabel = ttk.Label(text='Загаловок задачи:', style='TLabel', font=("Arial", 14))
titleLabel.pack(anchor=NW, padx=15)
titleInput = ttk.Entry()
titleInput.pack(anchor=N, fill=X, padx=15, pady=10, ipadx=5, ipady=5)

subtitleLabel = ttk.Label(text='Описание задачи:', style='TLabel', font=("Arial", 14))
subtitleLabel.pack(anchor=NW,padx=15)
subtitleInput = ttk.Entry()
subtitleInput.pack(anchor=N, fill=X, padx=15, pady=10, ipadx=5, ipady=5)

sendBtn = ttk.Button(root, text='Добавить', style="Green.TButton", command=getToDoData)
sendBtn.pack(fill=X, padx=15, pady=15, ipadx=5, ipady=5)

listToDoList = Listbox(root, font=('Arial', 15), bg='#444')
listToDoList.pack(anchor=N, fill=X, expand=True, padx=15)
listToDoList.bind('<<ListboxSelect>>', deleteList)

deleteBtn = ttk.Button(root,  text='Удалить', style="Red.TButton", command=deleteTask)
root.bind("<Delete>", deleteTask)


root.mainloop()
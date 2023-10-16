from tkinter import *


def add_task():
    task = input_entry.get()
    if task:
        task_list.insert(END, task)
        input_entry.delete(0, END)


def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)



def edit_task():
    selected_task = task_list.get(ACTIVE)
    updated_task = input_entry.get()

    if selected_task and updated_task:
        index = task_list.get(0, END).index(selected_task)
        task_list.delete(index)
        task_list.insert(index, updated_task)
        input_entry.delete(0, END)
    else:
        error.config(text="Please select a task to edit.")


root = Tk()
root.title("To-Do List")

main_label = Label(root,text="Enter Your Task Here..")
main_label.pack()
input_entry = Entry(root, width=30, bg="light green", fg="black")
input_entry.pack(pady=1)

add_btn = Button(root, text="Add Task", command=add_task, bg="gold")
add_btn.pack()


task_list = Listbox(root, width=30, bg="Gray", fg="white")
task_list.pack()

edit_btn = Button(root, text="Edit Task", command=edit_task,bg="gold")
edit_btn.pack()

error = Label(root, text="", fg="red")
error.pack()


delete_button = Button(root, text="Delete Task", command=delete_task, bg="gold")
delete_button.pack()


root.mainloop()
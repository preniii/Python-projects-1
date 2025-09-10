import tkinter as tk
from tkinter import messagebox #For pop-up messages

window = tk.Tk()
window.title("To Do List")
window.geometry("400x400")

entry= tk.Entry(window, width=40, font=("Arial",14))
entry.pack(pady=10) #entry box doesn't stick to other elements


listbox= tk.Listbox(window, width=40, height=10, font=("Arial",12))
listbox.pack(pady=10)

def add_task():
    task= entry.get()
    if task.strip() != "": #checks if the user actually entered something (not just spaces)
        listbox.insert(tk.END, task) #inserts task at the end of the listbox
        entry.delete(0, tk.END) #clears the entry box
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    selected_index =listbox.curselection() #gets the index of the selected item
    if selected_index:
        listbox.delete(selected_index[0]) #deletes the selected item
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")



add_button = tk.Button(window, text="Add task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete task", command=delete_task)
delete_button.pack(pady=5)


window.mainloop()

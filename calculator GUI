import tkinter as tk    #Creates windows,buttons, text boxes
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x300")


entry= tk.Entry(window, borderwidth=20, font= ("Arial", 18))
entry.grid(row=0, column =0, columnspan=4)

def button_press(value): #Adds a number or operator to the display when a button is pressed
    entry.insert(tk.END,value) #inserts value at the end of the current text

def button_clear(): #Clears the display
    entry.delete(0, tk.END) #deletes text from position 0 to the end

def button_equal(): #evaluates the expression in the display when = is pressed
    try: #catches errors like invalid expressions ("12++3")
        result= eval(entry.get()) 
        entry.delete(0,tk.END) 
        entry.insert(tk.END, str(result)) #inserts the result at the end of the display
    except:
        entry.delete(0,tk.END)
        entry.insert(tk.END, "Error")



buttons = [("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),  # (text, row, column)
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),]


tk.Button(window, text="C", height=2, borderwidth=3,   #Clear button
          command= button_clear).grid(row=5,column=0,columnspan=4, sticky="we") 


for (text, row, col) in buttons: #Creates buttons in a loop
    if text== "=":
        tk.Button(window, text=text, width=5, height =2, 
                  command= button_equal).grid(row=row, column=col)
    else:
        tk.Button(window, text=text, width=5, height=2, 
                  command=lambda t=text: button_press(t)).grid(row=row, column=col)




window.mainloop() #Starts the GUI event loop

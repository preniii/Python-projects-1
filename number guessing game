import tkinter as tk
import random #for generating random numbers

window= tk.Tk()
window.title("Number Guessing Game")
window.geometry("400x400")

number_to_guess= random.randint(1,100) #random number between 1 and 100
attempts=0#to count the number of attempts

entry= tk.Entry(window, width=20, font=("Arial",14))
entry.pack(pady=10)

result_label=tk.Label(window, text="", font=("Arial", 14)) #label to show results
result_label.pack(pady=5)

def check_guess(): #function to check the user's guess
    global attempts, number_to_guess ##doesn't create new variable with this name, uses the one I defined outside
    try:
        guess= int(entry.get())
        attempts= attempts+1
        if guess< number_to_guess:             
             result_label.config(text= "Too low! Try again.")
        elif guess> number_to_guess:
             result_label.config(text="Too high! Try again.")
        else:
             result_label.config(text="Congratulations! You guessed it in " + str(attempts) +" attempts!")             
    except ValueError: #handles non-integer inputs
         result_label.config(text="Please enter a valid number.")

guess_button = tk.Button(window, text="Guess", width=10, height=2, command=check_guess) #button to check the guess
guess_button.pack(pady=5)


def reset_game(): #function to reset the game
    global attempts, number_to_guess #doesn't create new variable with this name, uses the one I defined outside
    number_to_guess= random.randint(1,100)    
    entry.delete(0,tk.END)
    result_label.config(text="Game reset! Start guessing.")


reset_button = tk.Button(window, text="Reset Game", width= 10, height= 2, command= reset_game) #button to reset the game
reset_button.pack(pady=5)



window.mainloop()

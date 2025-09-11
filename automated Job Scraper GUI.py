import requests
from bs4 import BeautifulSoup #to read and parse HTML
import pandas as pd #to handle data and save to CSV
import tkinter as tk
from tkinter import messagebox, ttk #ttk for nicer widgets

url= "https://realpython.github.io/fake-jobs/"

def scrape_jobs():
    try:
        response= requests.get(url)
        if response.status_code !=200:
            messagebox.showerror("Error", "Failed to retrieve data")
            return
        html_doc= BeautifulSoup(response.text, "html.parser") #response.text contains the HTML content of the page. BeautifulSoup(..., "html.parser") → reads the HTML and turns it into a structure Python can understand.
        job_list=[] #list to hold job data
        job_cards = html_doc.find_all("div", class_="card-content") #find all job cards
        for card in job_cards:
            title = card.find("h2", class_="title").text.strip() #text.strip() removes extra spaces
            company = card.find("h3", class_="company").text.strip() #h2,h3,p are HTML tags
            location = card.find("p", class_="location").text.strip()
            job_list.append({
                "Title": title,
                "Company": company,
                "Location": location
            })
            
        df = pd.DataFrame(job_list) #convert list to DataFrame. like excel in python.
        df.to_csv("jobs.csv", index=False) #save to CSV without index column

        for row in tree.get_children(): #gives list of all rows currently in table
            tree.delete(row) #delete each row to clear old results before showing new jobs
        for _, row in df.iterrows(): #goes row by row through dataframe. _ is row index which we don't need.
            tree.insert("", "end", values=(row["Title"], row["Company"], row["Location"]))

        messagebox.showinfo("Success", f"{len(df)} Jobs saved to CSV!") #popup telling user how many jobs were saved

    except Exception as e: #Exception is a built-in Python class for any kind of error.
        messagebox.showerror("Error", f"An error occurred: {e}") 


window=tk.Tk()
window.title("Job scraper")
window.geometry("700x400")


job_button= tk.Button(window, text= "scrape jobs", font=("Arial",14), command= scrape_jobs)
job_button.pack(pady=20)
columns= ("Title", "Company", "Location")
tree= ttk.Treeview(window,columns=columns, show= "headings") #ttk.Treeview=table in GUI. show="headings" only shows column headings.
for col in columns:
    tree.heading(col, text=col) #set column headings
    tree.column(col, width=200) #set column width
tree.pack(pady=10)

scrape_jobs() 

window.mainloop()

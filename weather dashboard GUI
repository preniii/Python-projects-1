import tkinter as tk
from tkinter import messagebox
import requests #to make API requests(talks to the internet)

window = tk.Tk()
window.title("Weather Dashboard")
window.geometry("400x200")

def get_weather():
    city=city_entry.get() #user types city name
    api_key= os.getenv("API_KEY") #unique key from openweathermap
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric" #units=metric for celsius
    try:
        response=requests.get(url) #sends a request to the API at the given URL
        if response.status_code==200: #status_code: website tells Python if request worked. 200=success. 404=city not found. 500=server error.     
            data= response.json() #converts the response to JSON format
            temp = data["main"]["temp"] #extracts temperature from JSON data.   Put url in a JSON viewer to see structure
            weather= data["weather"][0]["description"] #gets text description of weather. 0=first item in list
            weather_label.config(text= f"{city}, {temp}\u00B0C , {weather}", fg="blue") #\u00B0 = degrees celsius symbol
        else:
            messagebox.showerror("Error", "City not found") #if not 200
    except:
        messagebox.showerror("Error","Unable to connect to the weather service") #if connection to internet or API fails
        


city_entry = tk.Entry(window, width=20, font=("Arial",14), fg="grey")
city_entry.insert(0, "Enter city...") #default text in entry box
city_entry.pack(pady=10)

get_weather_button= tk.Button(window, text="Get Weather", font=("Arial", 14), command=get_weather)
get_weather_button.pack(pady=10)

weather_label=tk.Label(window, text="", font=("Arial",14))
weather_label.pack(pady=10)

window.mainloop()

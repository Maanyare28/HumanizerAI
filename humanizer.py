import pswd
from google import genai
import tkinter as tk
from tkinter import ttk



TextToBeHumanized = input("Enter text you want humanized: ")
MakeItSoundHumanish = "Make this sound more casual, a bit informal, do not give me options just reply with the informal text: "
client = genai.Client(api_key=pswd.gemapikey)
response = client.models.generate_content(
model="gemini-2.0-flash",
contents=MakeItSoundHumanish + TextToBeHumanized
)
print(response.text)






# Create a python window
# root = tk.Tk() #basically we make it so instead of always calling tk we just call root
# root.title("Translater") #name of the window
# root.geometry("550x600") #window size


#Create Widgets


# root.mainloop()
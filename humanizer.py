import pswd
from google import genai
import tkinter as tk
from tkinter import ttk


def humanizer():

    TextToBeHumanized = "Take this text: " + textToHumanizeBox.get("1.0", tk.END).strip()
    HumanizeIt = "And humanize it, give me ONLY the humanized text"

    client = genai.Client(api_key=pswd.gemapikey)
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=TextToBeHumanized + HumanizeIt
    )
    textHumanizedBox.delete("1.0", tk.END)
    textHumanizedBox.insert(tk.END, response.text)






# Create a python window
root = tk.Tk() #basically we make it so instead of always calling tk we just call root
root.title("Humanizer") #name of the window
root.geometry("550x600") #window size


#Create Widgets
textToHumanizeBox = tk.Text(root, height=15, width=30)
textToHumanizeBox.place(x=5, y=50)

#Text Translated Box
textHumanizedBox = tk.Text(root, height=15, width=30)
textHumanizedBox.place(x=300, y=50)

#Button
humanizeButton = tk.Button(root, text="Humanize", command=humanizer)
humanizeButton.place(x=235,y=320)

root.mainloop()

# File Uploading
# Flask
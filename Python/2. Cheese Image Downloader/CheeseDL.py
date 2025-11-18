# Imports urllib to download the images
import urllib.request
# Imports TKInter for directory selection
import tkinter as tk
from tkinter import filedialog

def select_directory():
    global dir
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory_path = filedialog.askdirectory()
    if platform.system() == "Linux":
        dir = directory_path + "/"
    root.destroy() # Close the hidden root window
    pass

print("Welcome to the cheese script!")
answer = str(input("Press any key to select what directory to download the cheese to"))
dir = str("nothin")
select_directory()
answer = int(input("How much cheese do you want?"))
total = answer
current = int(0)
while current <= total:
    urllib.request(url, "cheese" + str(current) + ".jpg")
    current = current + 1
print("Enjoy the cheese!")
answer = str(input("Press any key to exit"))
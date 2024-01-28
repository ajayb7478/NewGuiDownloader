# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from tkinter import Tk, Canvas, Button, PhotoImage, Label, ttk
from pathlib import Path
import requests
from tqdm import tqdm
import selenium_auto_downloader
import automatic_deleter
import version_checker
import zip_extractor
import exe_launcher
from PIL import Image, ImageTk
import sys
import os
from link_downloader import download_and_read_link

text_widget = None

def update_text(message):
    text_label.config(text=message)

def disable_button():
    button_1.config(state="disabled")

def enable_button():
    button_1.config(state="normal")

def download_file_with_progress(url, destination, progress_bar):
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('content-length', 0))

    # Define the chunk size for downloading
    chunk_size = 1024  # 1 KB

    # Create a progress bar using ttk.Progressbar
    progress_bar['maximum'] = file_size
    progress_bar['value'] = 0

    os.makedirs(os.path.dirname(destination), exist_ok=True)

    with open(destination, 'wb') as file:
        for data in response.iter_content(chunk_size=chunk_size):
            progress_bar['value'] += len(data)
            file.write(data)
            
            # Update the GUI every 10 milliseconds
            window.update()

    progress_bar['value'] = file_size

# Replace 'your_link_here' with the actual link you have
file_url = download_and_read_link()

# Specify the directory where the file should be saved
download_directory = 'Downloads'

# Specify the file name
file_name = 'Rocket Flyer.zip'

# Combine the directory and file name to get the full destination path
destination_file_name = os.path.join(download_directory, file_name)

def check_for_updates():
    if version_checker.check_version():
        update_text("New Build Available. Downloading...")

        progress_bar = ttk.Progressbar(window, orient="horizontal", length=400, mode="determinate")
        progress_bar.place(x=5, y=460, width=400, height=20)

        try:
            download_file_with_progress(file_url, destination_file_name, progress_bar)       
            update_text("Installing...")
            zip_extractor.unzipper()
            automatic_deleter.delete_and_execute()
            update_text("Build is now on the latest version.")
            progress_bar.destroy()
            enable_button()
        except Exception as e:
            # Include the exception message in the update_text call
            update_text(f"Unable to download. Error")
            disable_button()  # Make sure to enable the button in case of failure
    else:
        update_text("Build is already on the latest version.")
        enable_button()


def launch_game():
    # Add any additional logic you may need before launching the game
    exe_launcher.game_launcher_script()

window = Tk()
window.title("")
window.iconbitmap("icon.ico")
#window.iconbitmap(default=sys._MEIPASS + "/icon.ico")

window.geometry("413x550")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 528,
    width = 413,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(file="image_1.png")
#image_image_1 = PhotoImage(file=Path(sys._MEIPASS) / "image_1.png")
image_1 = canvas.create_image(
    206.0,
    37.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file="image_2.png")
#image_image_2 = PhotoImage(file=Path(sys._MEIPASS) / "image_2.png")
image_2 = canvas.create_image(
    206.0,
    233.0,
    image=image_image_2
)

button_image_1 = PhotoImage(file="button_1.png")
#button_image_1 = PhotoImage(file=Path(sys._MEIPASS) / "button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: exe_launcher.game_launcher_script(),
    relief="flat"
)

button_1.place(
    x=89.0,
    y=500.0,
    width=235.0,
    height=38.0
)

disable_button()


text_label = Label(
    window,
    text="Checking for updates",
    bg="#FFFFFF",
    fg="#000000",
    font=("Arial", 12),
    bd=0,
    highlightthickness=0,
    relief="flat"
)
text_label.place(x=10, y=420.0, width=413.0, height=30.0)

canvas.create_rectangle(
    0.0,
    409.0,
    413.0,
    448.0,
    fill="#ffffff",
    outline="")

update_text("Checking for updates")
# Call check_for_updates after a delay (e.g., 100 milliseconds)
window.after(1000, check_for_updates)
window.resizable(False, False)
window.mainloop()
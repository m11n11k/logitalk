from string import whitespace

from customtkinter import *
from PIL import Image
from tkinter import filedialog
import requests

def send_file():
    filepath = filedialog.askopenfilename(title="Оберіть файл")
    if filepath:
        with open(filepath, "rb") as f:
            files = {"file": f}
            response = requests.post("http://127.0.0.1:5000/upload", files=files)


window  = CTk()
window.geometry('410x500')
window.title('chat_N.A.S.C.H.')
window.configure(fg_color='yellow')
img = CTkImage(Image.open("paper_clip.png"), size=(25,25))
btn_files = CTkButton(window, image = img, text = "", command=send_file,width=40,height=40,fg_color='white',hover_color='gray')
btn_files.pack(pady=100)
window.mainloop()
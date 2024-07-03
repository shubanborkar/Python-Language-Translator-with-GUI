from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1366x768')
root.resizable(0, 0)
root.title("Language Translator")

background_image = Image.open("/Users/shubanborkar/Desktop/Python MPR/Background.jpg")
image = background_image.resize((1366, 768))
background = ImageTk.PhotoImage(image)
background_label = Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(root, text="LANGUAGE TRANSLATOR", font="Times 30 bold", bg='black').pack()
Label(root, text="Project by Shuban, Pratham and Soham", font='Times 20 bold', width='35', bg='black').pack(side='bottom')

Label(root, text="Enter Text", font='Times 35 bold', bg='black').place(x=250, y=60)
Input_text = Text(root, font='Times 20', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=170)

Label(root, text="Output", font='Times 35 bold', bg='black').place(x=950, y=60)
Output_text = Text(root, font='Times 20', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=700, y=170)

language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values=language, width=22)
src_lang.place(x=220, y=120)
src_lang.set('Select Input Language')

dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=900, y=120)
dest_lang.set('Select Output Language')

def Translate():
    translator = Translator()
    input_text = Input_text.get(1.0, END)
    translated = translator.translate(text=input_text, src=src_lang.get(), dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

trans_btn = Button(root, text='Translate', font='Times 40 bold', pady=5, command=Translate, bg='Black')
trans_btn.place(x=600, y=550)

root.mainloop()

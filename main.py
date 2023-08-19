from tkinter import *
from tkinter import ttk
import googletrans
from googletrans import Translator

root = Tk()
root.title("Language Translator")
root.geometry("1060x400")
root.resizable(False, False)
root.configure(background="#FFFFFF")


# to change the label of selected language
def label_change():
    fr = from_lang.get()
    to = to_lang.get()
    from_label.configure(text=fr)
    to_label.configure(text=to)
    root.after(1000, label_change)


# to translate to chosen language
def translate_now():
    text = from_text.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text, src=from_lang.get(), dest=to_lang.get())
    translated_text = trans_text.text

    to_text.delete(1.0, END)
    to_text.insert(END, translated_text)


# translate image
icon = PhotoImage(file="trans.png")
root.iconphoto(False, icon)

convert = PhotoImage(file="convert.png")
img_label = Label(root, image=convert, width=250)
img_label.place(x=400, y=60)


# list of languages
lang = googletrans.LANGUAGES
lang_list = list(lang.values())
lang_dict = lang.keys()


# from language
from_lang = ttk.Combobox(root, values=lang_list, font=("Robote", 14), state="r")
from_lang.place(x=90, y=20)
from_lang.set("ENGLISH")

from_label = Label(root, text="ENGLISH", font=("segoe", 25, "bold"), bg="#FFFFFF", width=18, bd=5, relief=GROOVE)
from_label.place(x=20, y=60)

# to language
to_lang = ttk.Combobox(root, values=lang_list, font=("Robote", 14), state="r")
to_lang.place(x=730, y=20)
to_lang.set("SELECT LANGUAGE")

to_label = Label(root, text="ENGLISH", font=("segoe", 25, "bold"), bg="#FFFFFF", width=18, bd=5, relief=GROOVE)
to_label.place(x=665, y=60)

# from frame and text
from_frame = Frame(root, bg="#000000", bd=5)
from_frame.place(x=20, y=120, width=370, height=210)

from_text = Text(from_frame, font=("Robote", 20), bg="#FFFFFF", relief=GROOVE, wrap= WORD)
from_text.place(x=0, y=0, width=360, height=200)

from_scroll = Scrollbar(from_frame)
from_scroll.pack(side="right", fill="y")

from_scroll.configure(command=from_text.yview)
from_text.configure(yscrollcommand=from_scroll.set)


# to frame and text
to_frame = Frame(root, bg="#000000", bd=5)
to_frame.place(x=665, y=120, width=370, height=210)

to_text = Text(to_frame, font=("Robote", 20), bg="#FFFFFF", relief=GROOVE, wrap= WORD)
to_text.place(x=0, y=0, width=360, height=200)

to_scroll = Scrollbar(to_frame)
to_scroll.pack(side="right", fill="y")

to_scroll.configure(command=to_text.yview)
to_text.configure(yscrollcommand=to_scroll.set)


# btn to translate
translate_btn = Button(root,text="Translate", font=("Roboto", 15), activebackground="#FFFFFF", cursor="hand2",
                       bd=1, width=10, height=2, bg="#000000", fg="#FFFFFF", command=translate_now)
translate_btn.place(x=465, y=260)


label_change()
root.mainloop()

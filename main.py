from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/french_words.csv")
#print(data)
#converting it to a dictionary using the to_dict method

#print(to_learn)
current_card = {}
to_learn = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    #print(current_card["French"])
    canva.itemconfig(card_title, text="French")
    canva.itemconfig(card_word, text=current_card["French"])

def flip_card():
    canva.itemconfig(card_title, text="English")
    canva.itemconfig(card_word, text=current_card["English"])
    
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
       
window.after(3000, func=flip_card)

canva = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canva.create_image(400, 263, image=card_front_img)
card_title = canva.create_text(400,150,text='Title', font=('ariel',40,'italic'))
card_word = canva.create_text(400,263,text="Word",font=('ariel',60,'bold'))
canva.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva.grid(row=0,column=0,columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img,cursor='hand2',bd=0,highlightthickness=0,
                     command=next_card)
unknown_btn.grid(row=1,column=0)

tick_img = PhotoImage(file="images/right.png")
known_btn = Button(image=tick_img,cursor='hand2',highlightthickness=0,
                   command=is_known)
known_btn.grid(row=1,column=1)

time.sleep(1)
next_card()
window.mainloop()


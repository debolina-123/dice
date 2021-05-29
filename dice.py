from tkinter import *
import random
root=Tk()
root.title("roll dice")
root.geometry("800x800")
label=Label(root,font=('consolas',250,'bold'),text='')
label.pack()
def rolldice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()
button=Button(root,font=('consolas',25,'bold'),text='roll dice',command=rolldice)
button.pack()
root.mainloop()

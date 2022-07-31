from tkinter import messagebox
import tkinter as tk
def onOK():
    msg = "Your height is {} cm !".format(myentry.get())
    messagebox.showinfo(title = 'Result', message = msg )  
root = tk.Tk()
root.title('Height caculator tool')
root.wm_attributes('-toolwindow', 'True')
root.geometry('300x70')
mylabel = tk.Label(root, text='Input your height ')
mylabel.place(x=0,y=5)
myentry = tk.Entry(root)
myentry.place(x=110,y=5)
mylabel = tk.Label(root, text='cm')
mylabel.place(x=260,y=5)
mybutton = tk.Button(root, text='       Xem       ' ,command=onOK)
mybutton.place(x=200,y=35)

root.mainloop()

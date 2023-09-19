import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self): # Sets up the gui box
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        # this section adds a menubar to the top of the gui box with an option to close the box.
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close', command=self.on_Closing) # method allows user to confirm is they want to close the window.
        
        self.filemenu.add_separator()

        self.filemenu.add_command(label='Close without question', command=exit)

        self.actionMenu = tk.Menu(self.menubar, tearoff=0)
        self.actionMenu.add_command(label='Show message', command=self.show_message)
        
        #Menubar items
        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.menubar.add_cascade(menu=self.actionMenu, label='Action')

        self.root.config(menu=self.menubar)


        self.label = tk.Label(self.root, text='My First GUI', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut) # shortcut is a function that will look for the keys pressed
        self.textbox.pack(padx=10, pady=10)

        self.check_State = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_State)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_Closing)

        self.root.mainloop() # used to keep the box open.

    def show_message(self):
        if self.check_State.get() == 0: #looks to see if checkbox is checked or not.
            print(self.textbox.get('1.0', tk.END)) #the 1.0 starts the get at the beginning of the text box messages
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event): #This sends message box when ctr return is pressed
        if event.state == 12 and event.keysym =='Return':
            self.show_message()

    def on_Closing(self): # Asks user if they really want to quit when the x is pressed.
        if messagebox.askyesno(title="Quit", message="Do you really want to quit"):
            self.root.destroy()
        
    def clear(self):
        self.textbox.delete('1.0', tk.END)



MyGUI()














#import turtle as t
#from random import random

#for i in range(100):
#    steps = int(random() * 100)
#    angle = int(random() * 360)
#    t.right(angle)
#    t.fd(steps)

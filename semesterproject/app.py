from tkinter import ttk
import tkinter as tk
from forms import Dashboard, CustomerBooking, CustomerDetails, CurrencyConverter, Staff, NumberofMembers,Services, Feedback

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = ('Century Gothic Bold', 14)
        self.title('Hotel Management System')
        self.geometry('1200x740')
        self.image = tk.PhotoImage(file='images/ic.png')
        self.iconphoto(False, self.image)

        style = ttk.Style()
        style.configure('BB.TFrame', background='#000000')
        style.configure('BG.TLabel', background='teal')
        style.configure('BB.TLabel', background='#000000')
        style.configure('FBBG.TLabel', foreground='black', background='gold', font=('Century Gothic Bold', 20))
        style.configure('FGBB.TLabel', foreground='gold', background='#3b3b3b', font=('Century Gothic Bold', 40))
        style.configure('FGBB2.TLabel', foreground='gold', background='#3b3b3b', font=('Century Gothic Bold', 14))
        style.configure('FGBB3.TLabel', foreground='gold', background='#3b3b3b', font=('Century Gothic Bold', 160))
        style.configure('FWBB.TLabel', foreground='white', background='#3b3b3b', font=('Century Gothic Bold', 14))
        style.configure('FWBB2.TLabel', foreground='white', background='#3b3b3b', font=('Century Gothic Bold', 20))
        style.configure('FWBB3.TLabel', foreground='white', background='#3b3b3b', font=('Century Gothic Bold', 12))
        style.configure('FWBB.TRadiobutton', foreground='white', background='#3b3b3b', font=('Century Gothic Bold', 14))
        style.configure('FB.TButton', foreground='black', font=('Century Gothic Bold', 12))

        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky='NSEW')

        self.no_of_customers = 0
        self.customer = list()
        self.customer_info_list = list()
        self.customer_feedback_list = list()

        self.staff_info_list = list()

        self.frames = dict()
        for fr in (Dashboard, CustomerBooking, CustomerDetails, CurrencyConverter, Staff, NumberofMembers, Services, Feedback):
            page_name = fr.__name__
            frame = fr(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='NSEW')

        self.show_frame('Dashboard')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


app = App()
app.mainloop()

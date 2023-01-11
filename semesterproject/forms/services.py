import tkinter as tk
from tkinter import ttk
from tkinter import *

class Services(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        frame = ttk.Frame(self, padding=(30, 15, 30, 15), style='BB.TFrame')
        photo_frame = ttk.Frame(frame, style='BB.TFrame')

        self.denko_logo = PhotoImage(file='images/logo1234.png')
        denko_logo_label = ttk.Label(frame, image=self.denko_logo, anchor='center', style='BG.TLabel')

        services_label = ttk.Label(
            frame,
            text='FOOD SERVICES',
            anchor='center',
            padding=(30, 15, 30, 15),
            style='FBBG.TLabel'
        )

        back_image_button = ttk.Button(
            photo_frame,
            text='←',
            style='FB.TButton'
        )

        self.menu_front = PhotoImage(file='images/menu_front.png')
        self.menu_label = ttk.Label(
            photo_frame,
            image=self.menu_front,
            anchor='center',
            padding=(30, 15, 30, 15),
            style='BB.TLabel'
        )

        forward_image_button = ttk.Button(
            photo_frame,
            text='→',
            style='FB.TButton',
            command=self.change_photo
        )

        back_button = ttk.Button(
            frame,
            text='← Back',
            command=lambda: controller.show_frame("Dashboard"),
            style='FB.TButton'
        )

        frame.grid(row=0, column=0, sticky='NSEW')

        denko_logo_label.grid(row=0, column=0, sticky='NSEW')
        services_label.grid(row=1, column=0, sticky='EW')

        photo_frame.grid(row=2, column=0, sticky='NSEW')
        self.menu_label.grid(row=0, column=1, sticky='NSEW')
        back_image_button.grid(row=0, column=0)
        forward_image_button.grid(row=0, column=2)

        back_button.grid(row=3, column=0, columnspan=2, sticky='EW', pady=(0, 10))

        photo_frame.columnconfigure((0, 1, 2), weight=1)

    def change_photo(self):
        self.menu_label.config(image=PhotoImage(file='images/menu_back.png'))

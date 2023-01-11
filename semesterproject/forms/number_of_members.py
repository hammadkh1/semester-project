from tkinter import ttk
from tkinter import *
import tkinter as tk

class NumberofMembers(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        frame = ttk.Frame(self, padding=(10, 10, 10, 10), style='BB.TFrame')
        logo_frame = ttk.Frame(frame, style='BB.TFrame')
        heading_label_frame = ttk.Frame(frame, style='BB.TFrame')
        both_frames = ttk.Frame(frame)
        left_frame = ttk.Frame(both_frames, style='BB.TFrame', padding=(10, 10, 10, 10))
        self.search_by_frame = ttk.Frame(left_frame, style='BB.TFrame')
        self.side_frame = ttk.Frame(left_frame, style='BB.TFrame')
        right_frame = ttk.Frame(both_frames, style='BB.TFrame', padding=(10, 10, 10, 10))
        button_frame = ttk.Frame(frame, padding=(10, 10,10, 10), style='BB.TFrame')
        both_button_frames = ttk.Frame(button_frame, style='BB.TFrame')

        self.denko_logo = PhotoImage(file='images/logo1234.png')
        denko_logo_label = ttk.Label(logo_frame, image=self.denko_logo, anchor='center', style='BG.TLabel')

        search_customer_heading = ttk.Label(
            heading_label_frame,
            text='SEARCH CUSTOMERS',
            anchor='center',
            padding=(1, 1, 1, 1),
            style='FBBG.TLabel'
        )
        no_of_members_heading = ttk.Label(
            heading_label_frame,
            text='NUMBER OF MEMBERS',
            anchor='center',
            padding=(1, 1, 1, 1),
            style='FBBG.TLabel'
        )

        self.search_by_variable = tk.StringVar()
        search_by = ttk.Combobox(
            self.search_by_frame,
            textvariable=self.search_by_variable,
            values=('Search By Name', 'Search By Email'),
            justify='center',
            state='readonly',
            font=('Century Gothic', 12)
        )
        search_by.set('--Search By--')

        self.search_entry_variable = tk.StringVar()
        search_by_entry = ttk.Entry(
            self.search_by_frame,
            textvariable=self.search_entry_variable,
            width=30,
            justify='center',
            font=('Century Gothic', 12)
        )

        keys = ['Name', 'Email', 'Phone', 'No. of Members', 'Check In', 'Check Out', 'Room', 'Bill']
        for i, key in enumerate(keys):
            side_label = ttk.Label(
                self.side_frame,
                text=f'{key} :',
                style='FWBB3.TLabel'
            )
            side_label.grid(row=i, column=0, sticky='E')

        self.name_variable = tk.StringVar()
        self.name_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.name_variable,
            width=40
        )
        self.name_entry.grid(row=0, column=1, sticky='W')

        self.email_variable = tk.StringVar()
        self.email_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.email_variable,
            width=40
        )
        self.email_entry.grid(row=1, column=1, sticky='W')

        self.phone_variable = tk.IntVar()
        self.phone_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.phone_variable,
            width=40
        )
        self.phone_entry.grid(row=2, column=1, sticky='W')

        self.no_of_members_variable = tk.IntVar()
        self.no_of_members_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.no_of_members_variable,
            width=40
        )
        self.no_of_members_entry.grid(row=3, column=1, sticky='W')

        self.check_in_variable = tk.StringVar()
        self.check_in_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.check_in_variable,
            width=40
        )
        self.check_in_entry.grid(row=4, column=1, sticky='W')

        self.check_out_variable = tk.StringVar()
        self.check_out_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.check_out_variable,
            width=40
        )
        self.check_out_entry.grid(row=5, column=1, sticky='W')

        self.room_variable = tk.StringVar()
        self.room_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.room_variable,
            width=40
        )
        self.room_entry.grid(row=6, column=1, sticky='W')

        self.bill_variable = tk.IntVar()
        self.bill_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.bill_variable,
            width=40
        )
        self.bill_entry.grid(row=7, column=1, sticky='W')

        there_are_caption = ttk.Label(
            right_frame,
            text=f'THERE ARE',
            anchor='center',
            style='FWBB2.TLabel'
        )

        self.no_of_members = ttk.Label(
            right_frame,
            text=f'0',
            anchor='center',
            style='FGBB3.TLabel'
        )

        no_of_members_caption = ttk.Label(
            right_frame,
            text=f'MEMBER(S) CURRENTLY,\n       IN OUR HOTEL',
            anchor='center',
            style='FWBB2.TLabel'
        )

        search_button = ttk.Button(
            both_button_frames,
            text='Search',
            command=self.linear_search,
            style='FB.TButton'
        )

        check_button = ttk.Button(
            both_button_frames,
            text='Check',
            command=self.no_of_customers_func,
            style='FB.TButton'
        )

        back_button = ttk.Button(
            button_frame,
            text='← Back',
            command=lambda: controller.show_frame("Dashboard"),
            style='FB.TButton'
        )

        frame.grid(row=0, column=0, sticky='NSEW')
        logo_frame.grid(row=1, column=0, sticky='NSEW')
        heading_label_frame.grid(row=2, column=0, sticky='NSEW')
        both_frames.grid(row=3, column=0, sticky='NSEW')
        both_button_frames.grid(row=0, column=0, sticky='NSEW')
        button_frame.grid(row=4, column=0, sticky='NSEW')

        left_frame.grid(row=0, column=0, sticky='NSEW')
        search_customer_heading.grid(row=0, column=0, sticky='EW')
        self.search_by_frame.grid(row=0, column=0, sticky='NSEW')
        search_by.grid(row=0, column=0, sticky='W')
        search_by_entry.grid(row=0, column=1, sticky='W')
        self.side_frame.grid(row=1, column=0, sticky='EW')

        right_frame.grid(row=0, column=1, sticky='NSEW')
        no_of_members_heading.grid(row=0, column=1, sticky='EW')
        there_are_caption.grid(row=0, column=0, sticky='EW')
        self.no_of_members.grid(row=1, column=0, sticky='EW')
        no_of_members_caption.grid(row=2, column=0, sticky='EW')

        denko_logo_label.grid(row=0, column=0, sticky='NSEW')
        search_button.grid(row=0, column=0, sticky='EW', pady=(0, 1))
        check_button.grid(row=0, column=1, sticky='EW', pady=(0, 1))
        back_button.grid(row=0, column=2, sticky='EW', pady=(0, 1))

        heading_label_frame.columnconfigure((0, 1), weight=1)
        both_frames.columnconfigure((0, 1), weight=1)
        button_frame.columnconfigure(0, weight=1)
        both_button_frames.columnconfigure((0, 1), weight=1)

        for child in left_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)

        for child in self.side_frame.winfo_children():
            child.grid_configure(padx=10, pady=8)

        for child in self.search_by_frame.winfo_children():
            child.grid_configure(padx=10, pady=8)

    def linear_search(self):
        if self.search_by_variable.get() == 'Search By Name':
            self._linear_search('Name')

        elif self.search_by_variable.get() == 'Search By Email':
            self._linear_search('Email')

    def _linear_search(self, search_by):
        for customer in self.controller.customer:
            if customer[search_by] == self.search_entry_variable.get():
                self.name_variable.set(customer['Name'])
                self.email_variable.set(customer['Email'])
                self.phone_variable.set(customer['Phone'])
                self.no_of_members_variable.set(customer['No. of Members'])
                self.check_in_variable.set(customer['Check In'])
                self.check_out_variable.set(customer['Check Out'])
                self.room_variable.set(customer['Room'])
                self.bill_variable.set(customer['Bill'])

    def no_of_customers_func(self):
        self.no_of_members.config(text=f'{self.controller.no_of_customers}')

from tkinter import ttk
from tkinter import *
import tkinter as tk

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Feedback(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.stack_pointer = None

        frame = ttk.Frame(self, padding=(25, 10, 25, 10), style='BB.TFrame')
        logo_frame = ttk.Frame(frame, style='BB.TFrame')
        feedback_frame = ttk.Frame(frame, padding=(25, 10, 25, 10), style='BB.TFrame')
        button_frame = ttk.Frame(frame, padding=(25, 10, 25, 10), style='BB.TFrame')
        input_frame = ttk.Frame(feedback_frame, padding=(25, 10, 25, 10), style='BB.TFrame')

        self.denko_logo = PhotoImage(file='images/logo1234.png')
        denko_logo_label = ttk.Label(logo_frame, image=self.denko_logo, anchor='center', style='BG.TLabel')

        feedback_heading_label = ttk.Label(
            feedback_frame,
            text='CUSTOMER FEEDBACK',
            anchor='center',
            padding=(10, 10, 10, 10),
            style='FBBG.TLabel'
        )

        feedback_caption_label = ttk.Label(
            feedback_frame,
            text='Your feedback matters us.',
            anchor='w',
            padding=(30, 15, 30, 0),
            style='FWBB.TLabel'
        )

        self.name_variable = tk.StringVar()
        name_label = ttk.Label(
            input_frame,
            text='Name :',
            style='FWBB.TLabel'
        )
        self.name_entry = ttk.Entry(
            input_frame,
            textvariable=self.name_variable,
            width=100
        )
        self.name_entry.focus()

        self.email_variable = tk.StringVar()
        email_label = ttk.Label(
            input_frame,
            text='Email :',
            style='FWBB.TLabel'
        )
        self.email_entry = ttk.Entry(
            input_frame,
            textvariable=self.email_variable,
            width=100
        )

        self.ratings_variable = tk.DoubleVar()
        scale_label = ttk.Label(
            input_frame,
            text='Rate Us :',
            style='FWBB.TLabel'
        )
        self.ratings_scale = tk.Scale(
            input_frame,
            orient='horizontal',
            from_=0,
            to=10,
            variable=self.ratings_variable,
            command=self.handle_scale_change,
            sliderrelief='flat',
            highlightbackground='gold',
            bg='#3b3b3b',
            fg='white',
            font=('Century Gothic Bold', 14)
        )
        self.ratings_label = ttk.Label(
            input_frame,
            style='FGBB2.TLabel'
        )

        self.feedback_variable = tk.StringVar()
        feedback_label = ttk.Label(
            input_frame,
            text='Feedback :',
            style='FWBB.TLabel'
        )
        feedback_entry = ttk.Entry(
            input_frame,
            width=80,
            textvariable=self.feedback_variable
        )

        submit_button = ttk.Button(
            button_frame,
            text='Submit',
            command=self.feedback,
            style='FB.TButton'
        )

        back_button = ttk.Button(
            button_frame,
            text='← Back',
            command=lambda: controller.show_frame("Dashboard"),
            style='FB.TButton'
        )

        frame.grid(row=0, column=0, sticky='NSEW')
        logo_frame.grid(row=0, column=0, sticky='NSEW')
        feedback_frame.grid(row=1, column=0, sticky='NSEW')
        button_frame.grid(row=2, column=0, sticky='NSEW')
        input_frame.grid(row=2, column=0, sticky='NSEW')

        denko_logo_label.grid(row=0, column=0, sticky='NSEW')
        feedback_heading_label.grid(row=0, column=0, sticky='EW')
        feedback_caption_label.grid(row=1, column=0, sticky='EW')

        name_label.grid(row=0, column=0, sticky='W')
        self.name_entry.grid(row=0, column=1)
        email_label.grid(row=1, column=0, sticky='W')
        self.email_entry.grid(row=1, column=1)
        scale_label.grid(row=2, column=0, sticky='EW')
        self.ratings_scale.grid(row=2, column=1, sticky='EW')
        self.ratings_label.grid(row=2, column=2, sticky='EW')
        feedback_label.grid(row=3, column=0, sticky='W')
        feedback_entry.grid(row=3, column=1)

        submit_button.grid(row=0, column=0, columnspan=2, sticky='EW', pady=(0, 10))
        back_button.grid(row=1, column=0, columnspan=2, sticky='EW', pady=(0, 10))

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        feedback_frame.columnconfigure(0, weight=1)
        feedback_heading_label.columnconfigure(0, weight=1)
        button_frame.columnconfigure(0, weight=1)

        for child in input_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def handle_scale_change(self, event):
        self.ratings_label.config(text=f'{self.ratings_scale.get()} / 10')

    def feedback(self):
        customer = dict()
        customer['Name'] = self.name_variable.get()
        customer['Email'] = self.email_variable.get()
        customer['Ratings'] = self.ratings_variable.get()
        customer['Feedback'] = self.feedback_variable.get()

        self.controller.customer_feedback_list.append(customer)
        self.push(customer)

    def push(self, customer):
        if not isinstance(customer, Node):
            customer = Node(customer)
        if self.is_empty():
            self.stack_pointer = customer
        else:
            customer.next = self.stack_pointer
            self.stack_pointer = customer

        print(customer.data)
        Feedback.write_to_file(self)

    @staticmethod
    def write_to_file(stack_list):
        with open('feedback.txt', 'a') as file:
            file.write(f'Stack: {stack_list}\n')

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            curr = self.stack_pointer
            self.stack_pointer = self.stack_pointer.next
            curr.next = None
            return f'Removed: {curr.data}'

    def is_empty(self):
        return self.stack_pointer is None

    def __str__(self):
        string = ''
        current = self.stack_pointer
        while current:
            string += f'{current.data}->'
            current = current.next
        if string:
            print(f'Lateset Feedback = {self.stack_pointer.data}')
            return f'[{string[:-2]}]'
        return '[]'

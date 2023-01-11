from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CustomerBooking(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.head = None
        self.tail = None

        frame = ttk.Frame(self, padding=(20, 10, 20, 10), style='BB.TFrame')
        customer_frame = ttk.Frame(frame, padding=(20, 10, 20, 10), style='BB.TFrame')
        enqueue_frame = ttk.Frame(customer_frame, padding=(0, 10, 0, 10), style='BB.TFrame')
        room_frame = ttk.Frame(customer_frame, padding=(0, 1, 0, 1), style='BB.TFrame')
        self.selected_room_frame = ttk.Frame(frame, padding=(10, 10, 10, 10), style='BB.TFrame')

        customer_booking_label = ttk.Label(
            enqueue_frame,
            text='CUSTOMER BOOKING',
            anchor='center',
            style='FBBG.TLabel'
        )

        self.total_bill = 0

        self.name_variable = tk.StringVar()
        name_label = ttk.Label(
            enqueue_frame,
            text='Name :',
            style='FWBB.TLabel'
        )
        self.name_entry = ttk.Entry(
            enqueue_frame,
            textvariable=self.name_variable,
            width=50
        )

        self.email_variable = tk.StringVar()
        email_label = ttk.Label(
            enqueue_frame,
            text='Email :',
            style='FWBB.TLabel'
        )
        self.email_entry = ttk.Entry(
            enqueue_frame,
            textvariable=self.email_variable,
            width=50
        )

        self.phone_variable = tk.IntVar()
        phone_label = ttk.Label(
            enqueue_frame,
            text='Phone # :',
            style='FWBB.TLabel'
        )
        self.phone_entry = ttk.Entry(
            enqueue_frame,
            textvariable=self.phone_variable,
            width=50
        )

        self.members_variable = tk.IntVar()
        members_label = ttk.Label(
            enqueue_frame,
            text='No. of Members :',
            style='FWBB.TLabel'
        )
        self.members_spinbox = ttk.Spinbox(
            enqueue_frame,
            textvariable=self.members_variable,
            from_=1,
            to=15,
            wrap=True,
            state='readonly',
            justify='center',
            command=self.cost,
            width=48
        )

        self.check_in_variable = tk.StringVar()
        check_in_label = ttk.Label(
            enqueue_frame,
            text='Check In :',
            style='FWBB.TLabel'
        )
        self.check_in_entry = DateEntry(
            enqueue_frame,
            width=48,
            textvariable=self.check_in_variable,
            year=2023
        )

        self.check_out_variable = tk.StringVar()
        check_out_label = ttk.Label(
            enqueue_frame,
            text='Check Out :',
            style='FWBB.TLabel'
        )
        self.check_out_entry = DateEntry(
            enqueue_frame,
            width=48,
            textvariable=self.check_out_variable,
            year=2023
        )

        select_room_label = ttk.Label(
            room_frame,
            text='SELECT ROOM',
            anchor='center',
            style='FBBG.TLabel',
        )

        self.room_variable = tk.StringVar()
        self.deluxe_radiobutton = ttk.Radiobutton(
            room_frame,
            text='Deluxe Suite',
            variable=self.room_variable,
            value='Deluxe',
            command=self.cost,
            style='FWBB.TRadiobutton'
        )
        self.silver_radiobutton = ttk.Radiobutton(
            room_frame,
            text='Silver Suite',
            variable=self.room_variable,
            value='Silver',
            command=self.cost,
            style='FWBB.TRadiobutton'
        )
        self.gold_radiobutton = ttk.Radiobutton(
            room_frame,
            text='Gold Suite',
            variable=self.room_variable,
            value='Gold',
            command=self.cost,
            style='FWBB.TRadiobutton'
        )
        self.platinum_radiobutton = ttk.Radiobutton(
            room_frame,
            text='Platinum Suite',
            variable=self.room_variable,
            value='Platinum',
            command=self.cost,
            style='FWBB.TRadiobutton'
        )

        total_bill_label = ttk.Label(
            customer_frame,
            text='Total Bill : ',
            style='FWBB.TLabel'
        )
        self.calculate_total_bill_label = ttk.Label(
            customer_frame,
            text='Rs. 0/=',
            style='FWBB.TLabel'
        )

        clear_button = ttk.Button(
            customer_frame,
            text='Clear',
            command=self.clear,
            style='FB.TButton'
        )
        submit_button = ttk.Button(
            customer_frame,
            text='Submit',
            command=self.customer_info,
            style='FB.TButton'
        )
        back_button = ttk.Button(
            customer_frame,
            text='← Back',
            command=lambda: controller.show_frame("Dashboard"),
            style='FB.TButton'
        )

        self.selected_room_label = ttk.Label(
            self.selected_room_frame,
            text='SELECTED ROOM',
            padding=(10, 10, 10, 10),
            anchor='center',
            style='FWBB2.TLabel'
        )
        self.suite_label = ttk.Label(
            self.selected_room_frame,
            text='',
            padding=(10, 10, 10, 10),
            anchor='center',
            style='FBBG.TLabel'
        )
        self.room_info_label = ttk.Label(
            self.selected_room_frame,
            text='',
            anchor='center',
            style='FGBB2.TLabel'
        )
        self.room_size_label = ttk.Label(
            self.selected_room_frame,
            anchor='center',
            style='FWBB.TLabel'
        )
        self.bed_size_label = ttk.Label(
            self.selected_room_frame,
            anchor='center',
            style='FWBB.TLabel'
        )
        self.room_size_value_label = ttk.Label(
            self.selected_room_frame,
            anchor='center',
            style='FGBB2.TLabel'
        )
        self.bed_size_value_label = ttk.Label(
            self.selected_room_frame,
            anchor='center',
            style='FGBB2.TLabel'
        )

        self.suite_image_label = ttk.Label(
            self.selected_room_frame,
            anchor='center',
            style='BB.TLabel'
        )

        frame.grid(row=0, column=0, sticky='NSEW')
        customer_frame.grid(row=0, column=0, sticky='NSEW')
        enqueue_frame.grid(row=0, column=0, columnspan=2, sticky='EW')
        room_frame.grid(row=1, column=0, columnspan=2, sticky='EW')
        self.selected_room_frame.grid(row=0, column=1, sticky='NSEW')
        total_bill_label.grid(row=2, column=0, sticky='W', pady=(20, 20))
        self.calculate_total_bill_label.grid(row=2, column=1, sticky='E', pady=(20, 20))
        clear_button.grid(row=3, column=0, columnspan=2, sticky='EW', pady=(0, 10))
        submit_button.grid(row=4, column=0, columnspan=2, sticky='EW', pady=(0, 10))
        back_button.grid(row=5, column=0, columnspan=2, sticky='EW', pady=(0, 10))

        customer_booking_label.grid(row=0, column=0, columnspan=2, sticky='EW')
        name_label.grid(row=1, column=0, sticky='W')
        self.name_entry.grid(row=1, column=1, sticky='E')
        email_label.grid(row=2, column=0, sticky='W')
        self.email_entry.grid(row=2, column=1, sticky='E')
        phone_label.grid(row=3, column=0, sticky='W')
        self.phone_entry.grid(row=3, column=1, sticky='E')
        members_label.grid(row=4, column=0, sticky='W')
        self.members_spinbox.grid(row=4, column=1, sticky='E')
        check_in_label.grid(row=5, column=0, sticky='W')
        self.check_in_entry.grid(row=5, column=1, sticky='E')
        check_out_label.grid(row=6, column=0, sticky='W')
        self.check_out_entry.grid(row=6, column=1, sticky='E')
        select_room_label.grid(row=0, column=0, columnspan=2, sticky='EW')
        self.deluxe_radiobutton.grid(row=1, column=0, columnspan=2, sticky='EW')
        self.silver_radiobutton.grid(row=2, column=0, columnspan=2, sticky='EW')
        self.gold_radiobutton.grid(row=1, column=1, columnspan=2, sticky='EW')
        self.platinum_radiobutton.grid(row=2, column=1, columnspan=2, sticky='EW')

        self.selected_room_label.grid(row=0, column=0, columnspan=2, sticky='EW')
        self.suite_label.grid(row=1, column=0, columnspan=2, sticky='EW')
        self.room_info_label.grid(row=2, column=0, sticky='W')
        self.suite_image_label.grid(row=3, column=0, columnspan=2, sticky='EW', pady=(20, 20))
        self.room_size_label.grid(row=4, column=0, sticky='EW')
        self.bed_size_label.grid(row=4, column=1, sticky='EW')
        self.room_size_value_label.grid(row=5, column=0, sticky='EW')
        self.bed_size_value_label.grid(row=5, column=1, sticky='EW')

        self.rowconfigure(0, weight=1)
        room_frame.columnconfigure(0, weight=1)

        for child in room_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)

        for child in enqueue_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.phone_variable.set(0)
        self.members_spinbox.set(1)
        self.room_variable.set(None)
        self.total_bill = 0
        self.calculate_total_bill_label.config(text=f'Rs. {self.total_bill}/=')
        self.suite_label.config(text='')
        self.room_info_label.config(text='')
        self.room_size_label.config(text='')
        self.bed_size_label.config(text='')
        self.room_size_value_label.config(text='')
        self.bed_size_value_label.config(text='')
        self.suite_image_label.config(image='')

    def cost(self):
        members_cost = self.members_variable.get() * 1000
        self.total_bill = members_cost
        if self.room_variable.get() == 'Deluxe':
            self.total_bill = 0
            self.total_bill += 5000 + members_cost

        elif self.room_variable.get() == 'Silver':
            self.total_bill = 0
            self.total_bill += 10000 + members_cost

        elif self.room_variable.get() == 'Gold':
            self.total_bill = 0
            self.total_bill += 16000 + members_cost

        elif self.room_variable.get() == 'Platinum':
            self.total_bill = 0
            self.total_bill += 25000 + members_cost

        self.room_info_details()

        self.calculate_total_bill_label.config(text=f'Rs. {self.total_bill}/=')

    def room_info_details(self):

        if self.room_variable.get() == 'Deluxe':
            self.room_size_label.config(text='Room size')
            self.bed_size_label.config(text='Bed size(s)')
            self.suite_label.config(text='DELUXE SUITE')
            self.room_info_label.config(
                text='Service Provided:\n\n\t- Breakfast\n\t- Tea\n\t- Wifi\nRs. 5,000/=')
            self.suite_image = PhotoImage(file='images/a-01.png')
            self.suite_image_label.config(image=self.suite_image)
            self.room_size_value_label.config(text='162 Sq feet')
            self.bed_size_value_label.config(text='1 King/Queen or Twin')

        elif self.room_variable.get() == 'Silver':
            self.room_size_label.config(text='Room size')
            self.bed_size_label.config(text='Bed size(s)')
            self.suite_label.config(text='SILVER SUITE')
            self.room_info_label.config(
                text='Service Provided:\n\n\t- Breakfast\n\t- Lunch & Tea\n\t- Wifi +TV''\nRs. 10,000/=')
            self.suite_image = PhotoImage(file='images/a-02.png')
            self.suite_image_label.config(image=self.suite_image)
            self.room_size_value_label.config(text='324 Sq feet')
            self.bed_size_value_label.config(text='1 King')

        elif self.room_variable.get() == 'Gold':
            self.room_size_label.config(text='Room size')
            self.bed_size_label.config(text='Bed size(s)')
            self.suite_label.config(text='GOLD SUITE')
            self.room_info_label.config(
                text='Service Provided:\n\n\t- Breakfast\n\t- Lunch & Tea\n\t- Wifi + Smart TV''\nRs. 16,000/=')
            self.suite_image = PhotoImage(file='images/a-03.png')
            self.suite_image_label.config(image=self.suite_image)
            self.room_size_value_label.config(text='630 Sq feet')
            self.bed_size_value_label.config(text='1 King/Queen or Twin')

        elif self.room_variable.get() == 'Platinum':
            self.room_size_label.config(text='Room size')
            self.bed_size_label.config(text='Bed size(s)')
            self.suite_label.config(text='PLATINUM SUITE')
            self.room_info_label.config(
                text='Service Provided:\n\n\t- Breakfast + Lunch & Dinner\n\t- Netflix\n\t- Wifi + PS5''\nRs. 25,000/=')
            self.suite_image = PhotoImage(file='images/a-04.png')
            self.suite_image_label.config(image=self.suite_image)
            self.room_size_value_label.config(text='630 Sq feet')
            self.bed_size_value_label.config(text='1 King/Queen + Beach View')

    def customer_info(self):
        customer = dict()
        customer['Name'] = self.name_variable.get()
        customer['Email'] = self.email_variable.get()
        customer['Phone'] = self.phone_variable.get()
        customer['No. of Members'] = self.members_variable.get()
        customer['Check In'] = self.check_in_variable.get()
        customer['Check Out'] = self.check_out_variable.get()
        customer['Room'] = self.room_variable.get()
        customer['Bill'] = self.total_bill

        self.controller.customer_info_list.append(customer)
        self.controller.customer.append(customer)
        self.enqueue(customer)

    def enqueue(self, customer):
        if not isinstance(customer, Node):
            customer = Node(customer)
        if self.is_empty():
            self.head = customer
            self.tail = customer
        else:
            self.tail.next = customer
        self.tail = customer

        print(customer.data)
        self.controller.no_of_customers += 1
        CustomerBooking.write_to_file(self)

    @staticmethod
    def write_to_file(queue_list):
        with open('customer_booking.txt', 'a') as file:
            file.write(f'Queue: {queue_list}\n')

    def __str__(self):
        string = ''
        current = self.head
        while current:
            string += f'{current.data}->'
            current = current.next
        if string:
            return f'[{string[:-2]}]'
        return '[]'

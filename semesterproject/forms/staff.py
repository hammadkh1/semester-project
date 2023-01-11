from tkinter import ttk
from tkinter import *
import tkinter as tk
from forms.staff_hash_table import AlgoHashTable

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Staff(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.head = None
        self.tail = None

        self.hash_table = AlgoHashTable(5)

        self.controller = controller
        self.iid = 0

        list_of_dictionary = [
            {'Staff Type': 'Room Cleaning', 'Staff ID': 231, 'Name': 'Ali', 'CNIC': 432219281192221,
             'Phone': 3212345678, 'Address': 'Karachi'},
            {'Staff Type': 'Room Service', 'Staff ID': 312, 'Name': 'Ahmed', 'CNIC': 432219281192232,
             'Phone': 3214729652, 'Address': 'Lahore'},
            {'Staff Type': 'Room Service', 'Staff ID': 230, 'Name': 'Najjam', 'CNIC': 4322192811985764,
             'Phone': 3214729634, 'Address': 'Islamabad'},
            {'Staff Type': 'Room Cleaning', 'Staff ID': 100, 'Name': 'Affan', 'CNIC': 432219281198565,
             'Phone': 3214729634, 'Address': 'Faisalabad'},
            {'Staff Type': 'Room Service', 'Staff ID': 144, 'Name': 'Daud', 'CNIC': 432219281176665,
             'Phone': 3204729644, 'Address': 'Multan'},
            {'Staff Type': 'Room Service', 'Staff ID': 128, 'Name': 'Shabbir', 'CNIC': 432219281235436,
             'Phone': 3224729646, 'Address': 'Quetta'},
            {'Staff Type': 'Room Cleaning', 'Staff ID': 295, 'Name': 'Bashir', 'CNIC': 432219281196345,
             'Phone': 3244223638, 'Address': 'Sukkur'},
        ]
        for item in list_of_dictionary:
            self.controller.staff_info_list.append(item)

        frame = ttk.Frame(self, padding=(25, 10, 25, 10), style='BB.TFrame')
        logo_frame = ttk.Frame(frame, style='BB.TFrame')
        heading_label_frame = ttk.Frame(frame, style='BB.TFrame')
        both_frames = ttk.Frame(frame)
        left_frame = ttk.Frame(both_frames, style='BB.TFrame', padding=(25, 10, 25, 10))
        self.side_frame = ttk.Frame(left_frame, style='BB.TFrame')
        right_frame = ttk.Frame(both_frames, style='BB.TFrame', padding=(25, 10, 25, 10))
        button_frame = ttk.Frame(frame, padding=(25, 10, 25, 10), style='BB.TFrame')
        both_button_frames = ttk.Frame(button_frame, style='BB.TFrame')
        self.denko_logo = PhotoImage(file='images/logo1234.png')
        denko_logo_label = ttk.Label(logo_frame, image=self.denko_logo, anchor='center', style='BG.TLabel')

        add_staff_heading = ttk.Label(
            heading_label_frame,
            text='ADD THE STAFF',
            anchor='center',
            padding=(25, 10, 25, 10),
            style='FBBG.TLabel'
        )
        display_staff_heading = ttk.Label(
            heading_label_frame,
            text='DISPLAY THE STAFF',
            anchor='center',
            padding=(25, 10, 25, 10),
            style='FBBG.TLabel'
        )

        keys = ['Staff Type', 'Staff ID', 'Name', 'CNIC', 'Phone', 'Address']
        for i, key in enumerate(keys):
            side_label = ttk.Label(
                self.side_frame,
                text=f'{key} :',
                style='FWBB.TLabel'
            )
            side_label.grid(row=i, column=0, sticky='E')

        self.staff_type_variable = tk.StringVar()
        self.staff_type = ttk.Combobox(
            self.side_frame,
            textvariable=self.staff_type_variable,
            values=('Room Cleaning', 'Room Service'),
            justify='center',
            state='readonly',
            font=('Century Gothic', 12)
        )
        self.staff_type.set('--Select Type--')

        self.staff_id_variable = tk.IntVar()
        self.staff_id_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.staff_id_variable,
            width=40
        )
        self.staff_id_entry.grid(row=1, column=1, sticky='W')

        self.name_variable = tk.StringVar()
        self.name_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.name_variable,
            width=40
        )
        self.name_entry.grid(row=2, column=1, sticky='W')

        self.cnic_variable = tk.IntVar()
        self.cnic_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.cnic_variable,
            width=40
        )
        self.cnic_entry.grid(row=3, column=1, sticky='W')

        self.phone_variable = tk.IntVar()
        self.phone_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.phone_variable,
            width=40
        )
        self.phone_entry.grid(row=4, column=1, sticky='W')

        self.address_variable = tk.StringVar()
        self.address_entry = ttk.Entry(
            self.side_frame,
            textvariable=self.address_variable,
            width=40
        )
        self.address_entry.grid(row=5, column=1, sticky='W')

        clear_button = ttk.Button(
            self.side_frame,
            text='Clear',
            command=self.clear,
            style='FB.TButton'
        )
        clear_button.grid(row=6, column=0, columnspan=2, sticky='EW')

        self.treeview = ttk.Treeview(
            right_frame,
            columns=tuple(keys),
            height=15
        )

        self.treeview.column('#0', width=0, stretch=NO)
        for i in range(len(keys)):
            self.treeview.column(f'{keys[i]}', anchor='center', width=110)

        self.treeview.heading('#0', text='#0')
        for i in range(len(keys)):
            self.treeview.heading(f'{keys[i]}', text=f'{keys[i]}')

        add_the_staff_button = ttk.Button(
            both_button_frames,
            text='Add Staff',
            command=self.staff_info,
            style='FB.TButton'
        )

        display_button = ttk.Button(
            both_button_frames,
            text='Display',
            command=self.display,
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
        add_staff_heading.grid(row=0, column=0, sticky='EW')
        self.staff_type.grid(row=0, column=1, sticky='W')
        self.side_frame.grid(row=1, column=0, sticky='EW')
        self.treeview.grid(row=0, column=0, sticky='NSEW')

        right_frame.grid(row=0, column=1, sticky='NSEW')
        display_staff_heading.grid(row=0, column=1, sticky='EW')

        denko_logo_label.grid(row=0, column=0, sticky='NSEW')
        add_the_staff_button.grid(row=0, column=0, sticky='EW', pady=(0, 10))
        display_button.grid(row=0, column=1, sticky='EW', pady=(0, 10))
        back_button.grid(row=2, column=0, columnspan=2, sticky='EW', pady=(0, 10))

        heading_label_frame.columnconfigure((0, 1), weight=1)
        both_frames.columnconfigure((0, 1), weight=1)
        button_frame.columnconfigure(0, weight=1)
        both_button_frames.columnconfigure((0, 1), weight=1)

        for child in left_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)

        for child in self.side_frame.winfo_children():
            child.grid_configure(padx=10, pady=8)

        self.treeview.bind("<Double-1>", self.on_double_click)

    def clear(self):
        self.staff_type.set('--Select Type--')
        self.staff_id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.cnic_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.address_entry.delete(0, END)

        for row in self.treeview.get_children():
            self.treeview.delete(row)

    def is_empty(self):
        return self.head is None

    def staff_info(self):
        staff = dict()
        staff['Staff Type'] = self.staff_type_variable.get()
        staff['Staff ID'] = self.staff_id_variable.get()
        staff['Name'] = self.name_variable.get()
        staff['CNIC'] = self.cnic_variable.get()
        staff['Phone'] = self.phone_variable.get()
        staff['Address'] = self.address_variable.get()

        print(staff)
        self.enqueue(staff)
        self.controller.staff_info_list.append(staff)

    def enqueue(self, staff):
        if not isinstance(staff, Node):
            staff = Node(staff)
        if self.is_empty():
            self.head = staff
            self.tail = staff
        else:
            self.tail.next = staff
        self.tail = staff

        self.hash_table.set_value(staff.data['Staff ID'], list(staff.data.items()))
        print(f'Get Staff ID (1234): {self.hash_table.get_value(1234)}')
        print(f'Hash Table: {self.hash_table}')
        Staff.write_to_file(self)

    @staticmethod
    def write_to_file(queue_list):
        with open('staff_details.txt', 'a') as file:
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

    def display(self):
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        sorted_dictionary = self.insertion_sort(self.controller.staff_info_list)

        for dictionary in sorted_dictionary:
            self.treeview.insert(parent='', index='end', iid=self.iid, values=tuple(dictionary.values()))
            self.iid += 1

    def insertion_sort(self, arr):
        for key in range(1, len(arr)):
            if arr[key]['Staff ID'] < arr[key - 1]['Staff ID']:
                j = key
                while j > 0 and arr[j]['Staff ID'] < arr[j - 1]['Staff ID']:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    j -= 1
        return arr

    def on_double_click(self, event):
        try:
            item_id = event.widget.focus()
            item = event.widget.item(item_id)
            values = item['values']
            self.staff_type_variable.set(values[0])
            self.staff_id_variable.set(values[1])
            self.name_variable.set(values[2])
            self.cnic_variable.set(values[3])
            self.phone_variable.set(values[4])
            self.address_variable.set(values[5])
        except IndexError:
            pass

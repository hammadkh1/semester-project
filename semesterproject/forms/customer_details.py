from tkinter import *
from tkinter import ttk

class CustomerDetails(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        frame = ttk.Frame(self, padding=(25, 10, 25, 10), style='BB.TFrame')
        logo_frame = ttk.Frame(frame, style='BB.TFrame')
        customer_details_label_frame = ttk.Frame(frame, style='BB.TFrame')
        self.table_frame = ttk.Frame(frame, padding=(25, 10, 25, 10), style='BB.TFrame')
        button_frame = ttk.Frame(frame, padding=(25, 10, 25, 10), style='BB.TFrame')
        self.denko_logo = PhotoImage(file='images/logo1234.png')
        denko_logo_label = ttk.Label(logo_frame, image=self.denko_logo, anchor='center', style='BG.TLabel')

        self.iid = 0

        customer_details_label = ttk.Label(
            customer_details_label_frame,
            text='CUSTOMER DETAILS',
            anchor='center',
            padding=(25, 10, 25, 10),
            style='FBBG.TLabel'
        )

        keys = ['Name', 'Email', 'Phone', 'No. of Members', 'Check In', 'Check Out', 'Room', 'Bill']
        self.treeview = ttk.Treeview(
            self.table_frame,
            columns=tuple(keys),
            height=15
        )

        self.treeview.column('#0', width=0, stretch=NO)
        for i in range(len(keys)):
            self.treeview.column(f'{keys[i]}', anchor='center', width=110)

        self.treeview.heading('#0', text='#0')
        for i in range(len(keys)):
            self.treeview.heading(f'{keys[i]}', text=f'{keys[i]}')

        display_button = ttk.Button(
            button_frame,
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
        customer_details_label_frame.grid(row=2, column=0, sticky='NSEW')
        self.table_frame.grid(row=4, column=0, sticky='NSEW')
        button_frame.grid(row=5, column=0, sticky='NSEW')

        denko_logo_label.grid(row=0, column=0, sticky='NSEW')
        customer_details_label.grid(row=0, column=0, sticky='EW')
        display_button.grid(row=0, column=0, columnspan=2, sticky='EW', pady=(0, 10))
        back_button.grid(row=1, column=0, columnspan=2, sticky='EW', pady=(0, 10))

        customer_details_label_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(0, weight=1)
        self.table_frame.columnconfigure(0, weight=1)
        self.treeview.grid(row=0, column=0, sticky='NSEW')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.controller.rowconfigure(0, weight=1)
        self.controller.columnconfigure(0, weight=1)

    def display(self):
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        sorted_dictionary = self.divide_arr(self.controller.customer_info_list)

        for dictionary in sorted_dictionary:
            self.treeview.insert(parent='', index='end', iid=self.iid, values=tuple(dictionary.values()))
            self.iid += 1

    def bubble_sort(self, list_of_dict):
        swap_happened = True
        while swap_happened:
            swap_happened = False
            for i in range(len(list_of_dict) - 1):
                if list_of_dict[i]['Name'] > list_of_dict[i + 1]['Name']:
                    swap_happened = True
                    list_of_dict[i], list_of_dict[i + 1] = list_of_dict[i + 1], list_of_dict[i]
        return list_of_dict

    def merge_sort(self, arr1, arr2):
        sorted_list = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i]['Name'] < arr2[j]['Name']:
                sorted_list.append(arr1[i])
                i += 1
            else:
                sorted_list.append(arr2[j])
                j += 1
        while i < len(arr1):
            sorted_list.append(arr1[i])
            i += 1
        while j < len(arr2):
            sorted_list.append(arr2[j])
            j += 1
        return sorted_list

    def divide_arr(self, arr):
        if len(arr) < 2:
            return arr
        else:
            middle = len(arr) // 2
            left_divide, right_divide = arr[:middle], arr[middle:]
            l1 = self.divide_arr(left_divide)
            l2 = self.divide_arr(right_divide)
            return self.merge_sort(l1, l2)

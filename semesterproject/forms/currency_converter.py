from tkinter import ttk
from tkinter import *
import tkinter as tk


class CurrencyConverter(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        frame = ttk.Frame(self, padding=(30, 15, 30, 15), style='BB.TFrame')
        logo_frame = ttk.Frame(frame, style='BB.TFrame')
        currency_converter_frame = ttk.Frame(frame, padding=(30, 15, 30, 15), style='BB.TFrame')
        currency_converter_label_frame = ttk.Frame(frame, padding=(30, 15, 30, 15), style='BB.TFrame')

        self.denko_logo = PhotoImage(file='images/logo1234.png')
        denko_logo_label = ttk.Label(logo_frame, image=self.denko_logo, anchor='center', style='BG.TLabel')

        self.rates = {
            'USD': 1,
            'CAD': 1.26,
            'EUR': 0.85,
            'AED': 3.67,
            'FJD': 2.08,
            'HKD': 7.78,
            'INR': 73.38,
            'JPY': 110.71,
            'PKR': 225.55,
            'RUR': 76.44,
            'SAR': 3.75
        }

        self.currencies_list = list(self.rates.keys())

        currency_converter_label = ttk.Label(
            currency_converter_label_frame,
            text='CURRENCY CONVERTER',
            anchor='center',
            padding=(30, 15, 30, 15),
            style='FBBG.TLabel'
        )

        self.one_currency_label = ttk.Label(
            currency_converter_label_frame,
            anchor='center',
            text='1 USD',
            padding=(30, 15, 30, 15),
            style='FWBB.TLabel'
        )

        self.number_currency_label = ttk.Label(
            currency_converter_label_frame,
            text=f'{self.rates.get("EUR")} EUR',
            anchor='center',
            style='FGBB.TLabel'
        )

        self.from_currency = tk.StringVar()
        self.to_currency = tk.StringVar()
        self.from_entry_variable = tk.IntVar()
        self.to_entry_variable = tk.IntVar()

        self.from_entry = ttk.Entry(
            currency_converter_frame,
            textvariable=self.from_entry_variable,
            width=40,
            justify='center',
            font=('Century Gothic', 12)
        )
        self.from_entry.focus()
        self.from_combobox = ttk.Combobox(
            currency_converter_frame,
            textvariable=self.from_currency,
            values=tuple(self.currencies_list),
            justify='center',
            state='readonly',
            font=('Century Gothic', 12)
        )
        self.from_combobox.set('USD')

        self.to_entry = ttk.Entry(
            currency_converter_frame,
            textvariable=self.to_entry_variable,
            width=40,
            justify='center',
            state='readonly',
            font=('Century Gothic', 12)
        )
        self.to_combobox = ttk.Combobox(
            currency_converter_frame,
            textvariable=self.to_currency,
            values=tuple(self.currencies_list),
            justify='center',
            state='readonly',
            font=('Century Gothic', 12)
        )
        self.to_combobox.set('EUR')

        back_button = ttk.Button(
            currency_converter_frame,
            text='← Back',
            style='FB.TButton',
            command=lambda: controller.show_frame("Dashboard")
        )

        frame.grid(row=0, column=0, sticky='NSEW')
        logo_frame.grid(row=0, column=0, sticky='NSEW')
        denko_logo_label.grid(row=0, column=0, sticky='NSEW')
        currency_converter_label_frame.grid(row=1, column=0, sticky='NSEW')
        currency_converter_frame.grid(row=2, column=0, sticky='NSEW')

        currency_converter_label.grid(row=0, column=0, sticky='EW')
        self.one_currency_label.grid(row=1, column=0, sticky='EW')
        self.number_currency_label.grid(row=2, column=0, sticky='EW')

        self.from_entry.grid(row=0, column=0, sticky='EW', ipady=4)
        self.from_combobox.grid(row=0, column=1, sticky='EW', ipady=4)
        self.to_entry.grid(row=1, column=0, sticky='EW', ipady=4)
        self.to_combobox.grid(row=1, column=1, sticky='EW', ipady=4)
        back_button.grid(row=2, column=0, columnspan=2, sticky='EW', pady=(0, 10))

        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1), weight=1)
        denko_logo_label.columnconfigure(0, weight=1)
        currency_converter_label_frame.columnconfigure(0, weight=1)
        currency_converter_frame.columnconfigure((0, 1), weight=1)

        self.from_entry.bind('<KeyPress>', self.currency_converter)
        self.from_entry.bind('<KeyRelease>', self.currency_converter)
        self.from_combobox.bind('<<ComboboxSelected>>', self.combobox_handler)
        self.to_combobox.bind('<<ComboboxSelected>>', self.combobox_handler)

        for child in currency_converter_frame.winfo_children():
            child.grid_configure(padx=(10, 10), pady=(10, 10))

        for child in self.winfo_children():
            child.grid_configure(padx=(10, 10), pady=(10, 10))

    def combobox_handler(self, event):
        try:
            self.one_currency_label.config(text=f"1 {self.from_combobox.get()} equals")
            if self.from_currency.get() != 'USD':
                usd = 1 / self.rates[self.from_combobox.get()]
                amount = usd * self.rates[self.to_currency.get()]
            else:
                amount = 1 * self.rates[self.to_currency.get()]
            self.number_currency_label.config(text=f"{amount} {self.to_currency.get()}")

        except KeyError:
            pass

    def currency_converter(self, event):
        try:
            if self.from_currency.get() != 'USD':
                usd = self.from_entry_variable.get() / self.rates[self.from_currency.get()]
                amount = usd * self.rates[self.to_currency.get()]
                self.to_entry_variable.set(f'{amount}')
            else:
                amount = self.from_entry_variable.get() * self.rates[self.to_currency.get()]
                self.to_entry_variable.set(f'{amount}')
        except TclError:
            pass

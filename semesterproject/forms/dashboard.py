from tkinter import ttk
from tkinter import *

class Dashboard(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.state('zoomed')

        frame = ttk.Frame(self, padding=(20, 10, 20, 10), style='BB.TFrame')
        upper_buttons_frame = ttk.Frame(frame, style='BB.TFrame')
        bottom_buttons_frame = ttk.Frame(frame, style='BB.TFrame')
        self.logo = PhotoImage(file='images/logo1234.png')
        logo_label = ttk.Label(frame, image=self.logo, style='BG.TLabel')

        customer_booking_photo_image = PhotoImage(file='images/cb.png')
        self.customer_booking_photo = customer_booking_photo_image.subsample(5, 5)
        customer_booking_button = ttk.Button(
            upper_buttons_frame,
            text='Customer Booking',
            image=self.customer_booking_photo,
            compound=TOP,
            command=lambda: controller.show_frame("CustomerBooking"),
            style='FB.TButton'
        )

        customer_details_photo_image = PhotoImage(file='images/customer_details.png')
        self.customer_details_photo = customer_details_photo_image.subsample(5, 5)
        customer_details_button = ttk.Button(
            upper_buttons_frame,
            text='Customer Details',
            image=self.customer_details_photo,
            compound=TOP,
            command=lambda: controller.show_frame("CustomerDetails"),
            style='FB.TButton'
        )

        currency_converter_photo_image = PhotoImage(file='images/currency_converter.png')
        self.currency_converter_photo = currency_converter_photo_image.subsample(6, 5)
        currency_converter_button = ttk.Button(
            upper_buttons_frame,
            text='Currency Converter',
            image=self.currency_converter_photo,
            compound=TOP,
            command=lambda: controller.show_frame("CurrencyConverter"),
            style='FB.TButton'
        )

        staff_details_photo_image = PhotoImage(file='images/staff.png')
        self.staff_details_photo = staff_details_photo_image.subsample(5, 5)
        staff_details_button = ttk.Button(
            upper_buttons_frame,
            text='Staff',
            image=self.staff_details_photo,
            compound=TOP,
            command=lambda: controller.show_frame("Staff"),
            style='FB.TButton'
        )

        number_of_members_photo_image = PhotoImage(file='images/members.png')
        self.number_of_members_photo = number_of_members_photo_image.subsample(6, 6)
        number_of_members_button = ttk.Button(
            bottom_buttons_frame,
            text='Number of Members',
            image=self.number_of_members_photo,
            compound=TOP,
            command=lambda: controller.show_frame("NumberofMembers"),
            style='FB.TButton'
        )

        services_photo_image = PhotoImage(file='images/service.png')
        self.services_photo = services_photo_image.subsample(4, 5)
        services_button = ttk.Button(
            bottom_buttons_frame,
            text='Food Services',
            image=self.services_photo,
            compound=TOP,
            command=lambda: controller.show_frame("Services"),
            style='FB.TButton'
        )

        feedback_photo_image = PhotoImage(file='images/feedback.png')
        self.feedback_photo = feedback_photo_image.subsample(5, 5)
        feedback_button = ttk.Button(
            bottom_buttons_frame,
            text='Feedback',
            image=self.feedback_photo,
            compound=TOP,
            command=lambda: controller.show_frame("Feedback"),
            style='FB.TButton'
        )

        frame.grid(row=0, column=0, sticky='NSEW')

        logo_label.grid(row=0, column=0, columnspan=4)

        upper_buttons_frame.grid(row=1, column=0, sticky='NSEW')
        customer_booking_button.grid(row=0, column=0)
        customer_details_button.grid(row=0, column=1)
        currency_converter_button.grid(row=0, column=2)
        staff_details_button.grid(row=0, column=3)

        bottom_buttons_frame.grid(row=2, column=0, sticky='NSEW')
        number_of_members_button.grid(row=0, column=0)
        services_button.grid(row=0, column=1)
        feedback_button.grid(row=0, column=2)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        frame.columnconfigure(0, weight=1)
        upper_buttons_frame.columnconfigure((0, 1, 2, 3), weight=1)
        bottom_buttons_frame.columnconfigure((0, 1, 2), weight=1)

        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=(10, 10))

        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=(10, 10))

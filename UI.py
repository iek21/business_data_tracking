from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from tkinter import messagebox

import Modbus_Tcp as mtcp
from settings import Variables
import database as db
import operation as op

v = Variables()
data = db.data()

control = True


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Data Tracking')
        self.geometry('900x600')

        self.select_comm = 0

        # communication Label
        self.comm_tittle = ttk.Label(self, text='Communication :')
        self.comm_tittle.place(relx=0.01, rely=0, relwidth=0.3, relheight=0.05)

        # Select Communication Label
        self.s3 = IntVar()

        self.rb1 = Radiobutton(text="Modbus TCP", variable=self.s3, value=1)
        self.rb1['command'] = self.select_communucation
        self.rb1.place(relx=0.01, rely=0.04, relwidth=0.11, relheight=0.05)

        self.rb2 = Radiobutton(text="Modbus RTU", variable=self.s3, value=2)
        self.rb2['command'] = self.select_communucation
        self.rb2.place(relx=0.01, rely=0.08, relwidth=0.11, relheight=0.05)

        ##TCP Input TOOL (Label - Enrty)
        self.tcp_tittle = ttk.Label(self, text='TCP')
        self.tcp_tittle.place(relx=0.19, rely=0, relwidth=0.3, relheight=0.05)

        self.label_tcp_port = ttk.Label(self, text='Port :')
        self.label_tcp_port.place(relx=0.19, rely=0.04, relwidth=0.1, relheight=0.05)

        self.label_tcp_ip = ttk.Label(self, text='Host :')
        self.label_tcp_ip.place(relx=0.19, rely=0.08, relwidth=0.1, relheight=0.05)

        self.entry_tcp_port = tk.Entry(width=18)
        self.entry_tcp_port.place(relx=0.27, rely=0.043, relwidth=0.1)
        self.entry_tcp_port.insert(END, 502)

        self.entry_tcp_ip = tk.Entry(width=18)
        self.entry_tcp_ip.place(relx=0.27, rely=0.083, relwidth=0.1)
        self.entry_tcp_ip.insert(END, "192.168.1.106")

        ##RTU Input TOOL (Label - Enrty)
        self.rtu_tittle = ttk.Label(self, text='RTU')
        self.rtu_tittle.place(relx=0.40, rely=0, relwidth=0.3, relheight=0.05)

        self.label_rtu_baud = ttk.Label(self, text='Baud :')
        self.label_rtu_baud.place(relx=0.40, rely=0.04, relwidth=0.1, relheight=0.05)

        self.label_rtu_parity = ttk.Label(self, text='Parity:')
        self.label_rtu_parity.place(relx=0.40, rely=0.08, relwidth=0.1, relheight=0.05)

        self.label_rtu_port_name = ttk.Label(self, text='Port\nName :')
        self.label_rtu_port_name.place(relx=0.40, rely=0.12, relwidth=0.1, relheight=0.05)

        self.combo_rtu_baud = Combobox(text="Baud")
        self.combo_rtu_baud["values"] = (
            "128000", "115200", "115200", "19200", "14400", "9600", "7200", "4800", "1200", "600")
        self.combo_rtu_baud.place(relx=0.45, rely=0.045, relwidth=0.1, relheight=0.03)

        self.combo_rtu_parity = Combobox(text="Parity")
        self.combo_rtu_parity["values"] = ("None", "Odd", "Even", "Mark", "Space")
        self.combo_rtu_parity.place(relx=0.45, rely=0.085, relwidth=0.1, relheight=0.03)

        self.entry_rtu_port_name = tk.Entry(width=18)
        self.entry_rtu_port_name.place(relx=0.45, rely=0.125, relwidth=0.1)

        self.label_rtu_data_bits = ttk.Label(self, text='Data Bits:')
        self.label_rtu_data_bits.place(relx=0.60, rely=0.04, relwidth=0.1, relheight=0.05)

        self.label_rtu_stop_bits = ttk.Label(self, text='Stop Bits:')
        self.label_rtu_stop_bits.place(relx=0.60, rely=0.08, relwidth=0.1, relheight=0.05)

        self.label_rtu_slave_id = ttk.Label(self, text='Slave ID:')
        self.label_rtu_slave_id.place(relx=0.60, rely=0.12, relwidth=0.1, relheight=0.05)

        self.combo_rtu_data_bits = Combobox(text="Data_Bits")
        self.combo_rtu_data_bits["values"] = ("8 Bits", "7 Bits")
        self.combo_rtu_data_bits.place(relx=0.67, rely=0.045, relwidth=0.1, relheight=0.03)

        self.combo_rtu_stop_bits = Combobox(text="Stop Bits")
        self.combo_rtu_stop_bits["values"] = ("None", "1 Bit", "1.5 Bits", "2 Bits")
        self.combo_rtu_stop_bits.place(relx=0.67, rely=0.085, relwidth=0.1, relheight=0.03)

        self.entry_rtu_slave_id = tk.Entry(width=18)
        self.entry_rtu_slave_id.place(relx=0.67, rely=0.125, relwidth=0.1)

        ## Connect Tool Disable
        self.label_tcp_port.config(state='disabled')
        self.entry_tcp_port.config(state='disabled')
        self.label_tcp_ip.config(state='disabled')
        self.entry_tcp_port.config(state='disabled')
        self.entry_tcp_ip.config(state='disabled')
        self.tcp_tittle.config(state='disabled')
        self.rtu_tittle.config(state='disabled')
        self.label_rtu_baud.config(state='disabled')
        self.label_rtu_parity.config(state='disabled')
        self.combo_rtu_baud.config(state='disabled')
        self.combo_rtu_parity.config(state='disabled')
        self.label_rtu_data_bits.config(state='disabled')
        self.label_rtu_stop_bits.config(state='disabled')
        self.combo_rtu_data_bits.config(state='disabled')
        self.combo_rtu_stop_bits.config(state='disabled')
        self.entry_rtu_slave_id.config(state='disabled')
        self.label_rtu_slave_id.config(state='disabled')
        self.label_rtu_port_name.config(state='disabled')
        self.entry_rtu_port_name.config(state='disabled')

        ##Connected - Disconnect Button
        self.connected_button = tk.Button(text="Connect", font="Verdana 9 bold")
        self.connected_button['command'] = self.connect_button_block
        self.connected_button.place(relx=0.82, rely=0.045)
        self.connected_button.config(height=1, width=9)

        self.disconnected_button = tk.Button(text="Disconnect", font="Verdana 9 bold")
        self.disconnected_button['command'] = self.disconnect_button_block
        self.disconnected_button.place(relx=0.82, rely=0.110)
        self.disconnected_button.config(height=1, width=9)

    def select_communucation(self):
        if self.s3.get() == 1:
            self.label_tcp_port.config(state='normal')
            self.entry_tcp_port.config(state='normal')
            self.label_tcp_ip.config(state='normal')
            self.entry_tcp_port.config(state='normal')
            self.entry_tcp_ip.config(state='normal')
            self.tcp_tittle.config(state='normal')
            self.rtu_tittle.config(state='disabled')
            self.label_rtu_baud.config(state='disabled')
            self.label_rtu_parity.config(state='disabled')
            self.combo_rtu_baud.config(state='disabled')
            self.combo_rtu_parity.config(state='disabled')
            self.label_rtu_data_bits.config(state='disabled')
            self.label_rtu_stop_bits.config(state='disabled')
            self.combo_rtu_data_bits.config(state='disabled')
            self.combo_rtu_stop_bits.config(state='disabled')
            self.entry_rtu_slave_id.config(state='disabled')
            self.label_rtu_slave_id.config(state='disabled')
            self.label_rtu_port_name.config(state='disabled')
            self.entry_rtu_port_name.config(state='disabled')
        elif self.s3.get() == 2:
            self.label_tcp_port.config(state='disabled')
            self.label_tcp_ip.config(state='disabled')
            self.entry_tcp_port.config(state='disabled')
            self.entry_tcp_ip.config(state='disabled')
            self.tcp_tittle.config(state='disabled')
            self.rtu_tittle.config(state='normal')
            self.label_rtu_baud.config(state='normal')
            self.label_rtu_parity.config(state='normal')
            self.combo_rtu_baud.config(state='normal')
            self.combo_rtu_parity.config(state='normal')
            self.label_rtu_data_bits.config(state='normal')
            self.label_rtu_stop_bits.config(state='normal')
            self.combo_rtu_data_bits.config(state='normal')
            self.combo_rtu_stop_bits.config(state='normal')
            self.entry_rtu_slave_id.config(state='normal')
            self.label_rtu_slave_id.config(state='normal')
            self.label_rtu_port_name.config(state='normal')
            self.entry_rtu_port_name.config(state='normal')

    # def on_closing(self):
    #     if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #         tk.Tk().destroy()
    #
    # def close(self):
    #     tk.Tk().protocol("WM_DELETE_WINDOW", self.on_closing)
    #     tk.Tk().mainloop()

    def connect_button_block(self):

        if self.s3.get():  ##TCP
            if self.s3.get() == 1:
                if self.entry_tcp_ip.get() and self.entry_tcp_port.get():
                    try:
                        if str(self.entry_tcp_ip.get()) and int(self.entry_tcp_port.get()):

                            com_control = mtcp.tcp_open_server(str(self.entry_tcp_ip.get()),
                                                               int(self.entry_tcp_port.get()),
                                                               1, True)
                            if com_control:
                                self.operation_select()

                    except:
                        messagebox.showinfo(v.unsuccessful_message, "Please fill in the required fields correctly")
                else:
                    messagebox.showinfo(v.unsuccessful_message,
                                        "Please make sure your host and port information is valid")

            elif self.s3.get() == 2:  ##RTU

                baud = self.combo_rtu_baud.get()
                parity = self.combo_rtu_parity.get()
                data_bits = self.combo_rtu_data_bits.get()
                stop_bits = self.combo_rtu_stop_bits.get()
                slave_id = self.entry_rtu_slave_id.get()
                port_name = self.entry_rtu_port_name.get()
                if baud and parity and data_bits and stop_bits and slave_id and port_name:
                    # RTU BLOCK YAZILACAK
                    # self.operation_select()
                    messagebox.showinfo(v.unsuccessful_message, "Feature not activated")
                else:
                    messagebox.showinfo(v.unsuccessful_message, "Please fill in the required fields correctly")
        else:
            messagebox.showinfo(v.unsuccessful_message, "Please select a connection type")

    def disconnect_button_block(self):

        if self.s3.get():
            if self.s3.get() == 1:  ##TCP
                if self.entry_tcp_ip.get() and self.entry_tcp_port.get():
                    try:
                        mtcp.tcp_open_server(self.entry_tcp_ip.get(), self.entry_tcp_port.get(), 0, True)
                    except:
                        messagebox.showinfo(v.unsuccessful_message, "You are not already connected")
                else:
                    messagebox.showinfo(v.unsuccessful_message, "You are not already connected")
            if self.s3.get() == 2:  ##RTU
                ##RTU DİSABLE YAZILACAK
                messagebox.showinfo(v.unsuccessful_message, "You are not already connected")
        else:
            messagebox.showinfo(v.unsuccessful_message, "You are not already connected")

    def operation_select(self):
        self.label_operation_select = ttk.Label(text='Add Register for Tracking:')
        self.label_operation_select.place(relx=0.01, rely=0.2, relwidth=0.3, relheight=0.05)

        self.combo_operation_select = Combobox(text="Data Tittle")
        self.combo_operation_select["values"] = ("Add Register", "Delete Register", "Scaning Register")
        self.combo_operation_select.place(relx=0.17, rely=0.21, relwidth=0.1, relheight=0.03)

        self.operation_select_button = tk.Button(text="Continue", font="Verdana 9 bold")
        self.operation_select_button['command'] = self.select_screen_helper
        self.operation_select_button.place(relx=0.29, rely=0.20)
        self.operation_select_button.config(height=1, width=9)

    def select_screen_helper(self):
        self.select_screen()

    def select_screen(self):
        select = self.combo_operation_select.get()
        if select == "Add Register" or select == "Delete Register" or select == "Scaning Register":
            if select == "Add Register":
                self.add_data(1)
            if select == "Delete Register":
                pass
            if select == "Scaning Register":
                pass
        else:
            messagebox.showinfo(v.unsuccessful_message, "Please make a choice")

    def add_data(self, open_clear):

        if open_clear == 1:
            self.label_regester_name = ttk.Label(self, text='Register Name     :')
            self.label_regester_name.place(relx=0.01, rely=0.26, relwidth=0.3, relheight=0.05)

            self.label_reading_type = ttk.Label(self, text='Reading Type :')
            self.label_reading_type.place(relx=0.01, rely=0.30, relwidth=0.3, relheight=0.05)

            self.label_regester_address = ttk.Label(self, text='Regester Address:')
            self.label_regester_address.place(relx=0.01, rely=0.35, relwidth=0.3, relheight=0.05)

            self.label_save_all_data = ttk.Label(self, text='Save All Data:')
            self.label_save_all_data.place(relx=0.01, rely=0.40, relwidth=0.3, relheight=0.05)

            self.label_save_sampled_data = ttk.Label(self, text='Save Sampled Data:')
            self.label_save_sampled_data.place(relx=0.01, rely=0.45, relwidth=0.3, relheight=0.05)

            self.label_range_of_word = ttk.Label(self, text='Saved Data Out\nRange of Work  :')
            self.label_range_of_word.place(relx=0.01, rely=0.50, relwidth=0.3, relheight=0.05)

            self.label_reporting_period = ttk.Label(self, text='Reporting Period  :')
            self.label_reporting_period.place(relx=0.01, rely=0.56, relwidth=0.3, relheight=0.05)

            self.label_email_reports = ttk.Label(self, text='Email Me\nthe Reports:')
            self.label_email_reports.place(relx=0.01, rely=0.61, relwidth=0.3, relheight=0.05)

            self.label_phone_natification = ttk.Label(self,
                                                      text=' * If it works out of range, get a notification on my phone :')
            self.label_phone_natification.place(relx=0, rely=0.67, relwidth=0.5, relheight=0.05)

            self.entry_regester_name = tk.Entry(width=18)
            self.entry_regester_name.place(relx=0.14, rely=0.27, relwidth=0.15)
            self.entry_regester_name.insert(END, "Give the address a name")

            self.combo_reading_type = Combobox(text="Data Type")
            self.combo_reading_type["values"] = (
                "Read Coils", "Read Holding Regester", "Read Discrete Inputs", "Read Input Regester")
            self.combo_reading_type.place(relx=0.14, rely=0.31, relwidth=0.15, relheight=0.03)

            self.entry_regester_address = tk.Entry(width=18)
            self.entry_regester_address.place(relx=0.14, rely=0.36, relwidth=0.15)

            self.var_save_data = IntVar()

            self.rb_save_all_data = Radiobutton(variable=self.var_save_data, value=1)
            self.rb_save_all_data.place(relx=0.19, rely=0.40, relwidth=0.11, relheight=0.05, anchor=N)
            self.rb_save_all_data['command'] = self.sampling_time

            self.rb_save_sampled_data = Radiobutton(variable=self.var_save_data, value=2)
            self.rb_save_sampled_data.place(relx=0.19, rely=0.45, relwidth=0.11, relheight=0.05, anchor=N)
            self.rb_save_sampled_data['command'] = self.sampling_time

            self.label_sampling_interval = ttk.Label(self, text='Sampling time:')
            self.label_sampling_interval.place(relx=0.195, rely=0.45, relwidth=0.35, relheight=0.05)
            self.label_sampling_interval.config(state='disabled')

            self.entry_sampling_interval = tk.Entry(width=18)
            self.entry_sampling_interval.place(relx=0.30, rely=0.46, relwidth=0.07)
            self.entry_sampling_interval.config(state='disabled')

            self.combo_sampling_interval = Combobox(text="Sampling time")
            self.combo_sampling_interval["values"] = ("Second", "Minute", "Hour", "Day")
            self.combo_sampling_interval.place(relx=0.38, rely=0.46, relwidth=0.07, relheight=0.03)
            self.combo_sampling_interval.config(state='disabled')

            self.var_range_of_word = IntVar()
            self.cb_range_of_word = Checkbutton(variable=self.var_range_of_word, onvalue=1, offvalue=0)
            self.cb_range_of_word['command'] = self.range_of_word
            self.cb_range_of_word.place(relx=0.19, rely=0.50, relwidth=0.11, relheight=0.05, anchor=N)

            self.entry_reporting_period = tk.Entry(width=18)
            self.entry_reporting_period.place(relx=0.14, rely=0.57, relwidth=0.07)

            self.combo_reporting_period = Combobox(text="Reporting Period")
            self.combo_reporting_period["values"] = ("Hour", "Day")
            self.combo_reporting_period.place(relx=0.22, rely=0.57, relwidth=0.07, relheight=0.03)

            self.var_email_reports = IntVar()
            self.cb_email_reports = Checkbutton(variable=self.var_email_reports, onvalue=1, offvalue=0)
            self.cb_email_reports['command'] = self.email_reports
            self.cb_email_reports.place(relx=0.19, rely=0.62, relwidth=0.11, relheight=0.05, anchor=N)

            self.var_phone_natification = IntVar()
            self.cb_phone_natification = Checkbutton(variable=self.var_phone_natification, onvalue=1, offvalue=0)
            self.cb_phone_natification['command'] = self.phone_natification
            self.cb_phone_natification.place(relx=0.40, rely=0.67, relwidth=0.11, relheight=0.05, anchor=N)

            self.saved_start_button = tk.Button(text="Save and Start Tracking", font="Verdana 9 bold")
            self.saved_start_button['command'] = self.saved_and_start_button
            self.saved_start_button.place(relx=0.05, rely=0.80)
            self.saved_start_button.config(height=1, width=20)

        if open_clear == 0:  ## Clear tool
            self.label_regester_name.place_forget()
            self.label_reading_type.place_forget()
            self.label_regester_address.place_forget()
            self.label_save_all_data.place_forget()
            self.label_save_sampled_data.place_forget()
            self.label_range_of_word.place_forget()
            self.label_reporting_period.place_forget()
            self.label_email_reports.place_forget()
            self.label_phone_natification.place_forget()
            self.entry_regester_name.place_forget()
            self.combo_reading_type.place_forget()
            self.entry_regester_address.place_forget()
            self.rb_save_all_data.place_forget()
            self.rb_save_sampled_data.place_forget()
            self.saved_start_button.place_forget()
            self.entry_reporting_period.place_forget()
            self.combo_reporting_period.place_forget()
            if self.var_range_of_word.get() == 1:
                self.label_range_of_word_min.place_forget()
                self.label_range_of_word_max.place_forget()
                self.entry_range_of_word_min.place_forget()
                self.entry_range_of_word_max.place_forget()
                self.label_range_of_word_warning.place_forget()
            if self.var_email_reports.get() == 1:
                self.label_email_address.place_forget()
                self.entry_email_address.place_forget()
            if self.var_phone_natification.get() == 1:
                self.label_phone_number.place_forget()
                self.entry_phone_number.place_forget()
            self.entry_sampling_interval.place_forget()
            self.combo_sampling_interval.place_forget()
            self.label_sampling_interval.place_forget()
            self.cb_range_of_word.place_forget()
            self.cb_email_reports.place_forget()
            self.cb_phone_natification.place_forget()

    def sampling_time(self):  ##select_screen subfunction
        if self.var_save_data.get() == 1:
            self.entry_sampling_interval.config(state='disabled')
            self.combo_sampling_interval.config(state='disabled')
            self.label_sampling_interval.config(state='disabled')
        if self.var_save_data.get() == 2:
            self.entry_sampling_interval.config(state='normal')
            self.combo_sampling_interval.config(state='normal')
            self.label_sampling_interval.config(state='normal')

    def range_of_word(self):  ##select_screen subfunction

        if self.var_range_of_word.get() == 1:
            self.label_range_of_word_min = ttk.Label(self, text='Min Value:')
            self.label_range_of_word_min.place(relx=0.195, rely=0.50, relwidth=0.35, relheight=0.05)

            self.label_range_of_word_max = ttk.Label(self, text='Max Value:')
            self.label_range_of_word_max.place(relx=0.37, rely=0.50, relwidth=0.35, relheight=0.05)

            self.label_range_of_word_warning = tk.Label(text="Enter the value range you\nwant the sensor to work in",
                                                        bg="red", fg="black", font="Verdana 12 bold")
            self.label_range_of_word_warning.place(relx=0.55, rely=0.50)

            self.entry_range_of_word_min = tk.Entry(width=18)
            self.entry_range_of_word_min.place(relx=0.28, rely=0.51, relwidth=0.07)

            self.entry_range_of_word_max = tk.Entry(width=18)
            self.entry_range_of_word_max.place(relx=0.45, rely=0.51, relwidth=0.07)

        elif self.var_range_of_word.get() == 0:
            self.label_range_of_word_min.place_forget()
            self.label_range_of_word_max.place_forget()
            self.entry_range_of_word_min.place_forget()
            self.entry_range_of_word_max.place_forget()
            self.label_range_of_word_warning.place_forget()

    def email_reports(self):  ##data_regester_screen subfunction

        if self.var_email_reports.get() == 1:
            self.label_email_address = ttk.Label(self, text='Email Adress:')
            self.label_email_address.place(relx=0.195, rely=0.62, relwidth=0.35, relheight=0.05)

            self.entry_email_address = tk.Entry(width=18)
            self.entry_email_address.place(relx=0.29, rely=0.63, relwidth=0.15)

        elif self.var_email_reports.get() == 0:
            self.label_email_address.place_forget()
            self.entry_email_address.place_forget()

    def phone_natification(self):  ##data_regester_screen subfunction

        if self.var_phone_natification.get() == 1:
            self.label_phone_number = ttk.Label(self, text='Phone Number:')
            self.label_phone_number.place(relx=0, rely=0.72, relwidth=0.35, relheight=0.05)

            self.entry_phone_number = tk.Entry(width=18)
            self.entry_phone_number.place(relx=0.14, rely=0.73, relwidth=0.15)

        elif self.var_phone_natification.get() == 0:
            self.label_phone_number.place_forget()
            self.entry_phone_number.place_forget()

    def saved_and_start_button(self):
        sampling_interval = "Not Entered"
        sampling_interval_unit = ""
        range_of_word_min = "Not Entered"
        range_of_word_max = "Not Entered"
        email_address = "Not Entered"
        phone_number = "Not Entered"

        sampling_interval_control = False
        range_of_word_min_control = False
        reg_address_control = False
        reporting_period_control = False

        if self.var_save_data.get() == 2:
            try:
                sampling_interval = int(self.entry_sampling_interval.get())
                sampling_interval_control = True
            except:
                messagebox.showinfo(v.unsuccessful_message, "Sampling time must be number")
            sampling_interval_unit = self.combo_sampling_interval.get()
        elif self.var_save_data.get() == 1:
            sampling_interval = "Not Entered"
            sampling_interval_unit = ""

        if self.var_range_of_word.get() == 1:
            try:
                range_of_word_min = int(self.entry_range_of_word_min.get())
                range_of_word_max = int(self.entry_range_of_word_max.get())
                range_of_word_min_control = True
            except:
                messagebox.showinfo(v.unsuccessful_message, "Max Value and Min Value must be number")
        elif self.var_range_of_word.get() == 0:
            range_of_word_min = "Not Entered"
            range_of_word_max = "Not Entered"

        if self.var_email_reports.get() == 1:
            email_address = self.entry_email_address.get()
        elif self.var_email_reports.get() == 0:
            email_address = "Not Entered"
        if self.var_phone_natification.get() == 1:
            phone_number = self.entry_phone_number.get()
        if self.var_phone_natification.get() == 0:
            phone_number = "Not Entered"
        try:
            self.reg_address = int(self.entry_regester_address.get())
            reg_address_control = True
        except:
            messagebox.showinfo(v.unsuccessful_message, "Registration address must be number")

        try:
            self.reporting_period = int(self.entry_regester_address.get())
            reporting_period_control = True
        except:
            messagebox.showinfo(v.unsuccessful_message, "Repording period must be number")

        if self.entry_regester_name.get() and self.combo_reading_type.get() and self.entry_regester_address.get() \
                and self.combo_reporting_period.get() and self.combo_reporting_period.get():
            if self.var_save_data.get() == 2 or self.var_save_data.get() == 1:
                if reg_address_control and reporting_period_control:
                    if sampling_interval_control or self.var_save_data.get() == 1:
                        if range_of_word_min_control or self.var_range_of_word.get() == 0:
                            reg_name_status = op.record_control_block(self.entry_regester_name.get())
                            if reg_name_status:
                                data.add_data(str(self.entry_regester_name.get()), str(self.entry_tcp_ip.get()),
                                              self.combo_reading_type.get(),
                                              self.reg_address,
                                              str(self.reporting_period) + " " + self.combo_reporting_period.get(),
                                              str(sampling_interval) + " " + sampling_interval_unit,
                                              range_of_word_max, range_of_word_min, str(email_address),
                                              str(phone_number))
                                self.server_list = op.data_tracking(str(self.entry_regester_name.get()), self.combo_reading_type.get(),
                                                 str(self.entry_tcp_ip.get()), int(self.entry_tcp_port.get()),
                                                 self.reg_address, self.var_save_data.get(), sampling_interval,
                                                 sampling_interval_unit, str(phone_number), self.var_phone_natification,
                                                 range_of_word_min, range_of_word_max)
                                print(self.server_list)
                                if self.cb_email_reports == 1:
                                    op.data_repording(1, str(self.entry_regester_name.get()),
                                                      self.entry_email_address.get(), self.reporting_period,
                                                      self.combo_reporting_period, range_of_word_min, range_of_word_max)
                                    if self.var_range_of_word == 1:
                                        op.data_repording(2, str(self.entry_regester_name.get()),
                                                          self.entry_email_address.get(), self.reporting_period,
                                                          self.combo_reporting_period,
                                                          range_of_word_min, range_of_word_max)
                                self.add_data(0)

            else:
                messagebox.showinfo(v.unsuccessful_message, "Please tick Data record type")
        else:
            messagebox.showinfo(v.unsuccessful_message, "Please fill in the fields")


if __name__ == "__main__":
    app = App()
    app.mainloop()

from pyModbusTCP.client import ModbusClient
from pyModbusTCP.server import ModbusServer
from tkinter import messagebox
import datetime
import time

from settings import Variables
from database import data
import operation as op

d = data()
v = Variables()


def tcp_open_server(ip, port, on_of, message_status):
    global host, c, server

    host = ip  ##"192.168.1.106"
    com_control = False

    try:
        c = ModbusClient(host=host, port=port, auto_open=True)  ##port 502
        server = ModbusServer(host=host, port=port, no_block=True)
    except:
        if on_of == 1:
            message_failed = "Unable to connect to " + host + ":502"
            if message_status:
                messagebox.showinfo(v.unsuccessful_message, message_failed)
        if on_of == 0:
            if message_status:
                messagebox.showinfo(v.successful_message, "You are not already connected")
            else:
                pass

    try:
        if on_of == 1:
            if not c.is_open():
                if server.is_run:
                    pass
                else:
                    server.start()
                if not c.is_open():
                    if not c.open():
                        if message_status:
                            message_failed = "Unable to connect to " + host + ":502"
                            messagebox.showinfo(v.unsuccessful_message, message_failed)
                if c.is_open():
                    if message_status:
                        messagebox.showinfo(v.successful_message, "Connection successful")
                    com_control = True
        if on_of == 0:
            server.stop()
            if message_status:
                messagebox.showinfo(v.successful_message, "Server is down")
    except:
        pass

    return com_control


def tcp_listen_line(reg_name, read_type, regester_address, ip, port, samplig_time, phone_number, phone_message_status,
                    range_min, range_max):
    global host, c

    try:  ## veri tabanından serverin açık oldp olmadığı kontrol edilecek eğer aynı server daha önce açılmışsa yeniden server açılmayacak
        tcp_open_server(ip, port, 0, False)
        tcp_open_server(ip, port, 1, False)
    except:
        messagebox.showinfo(v.successful_message, "Server is open" + v.successful_message)

    while True:

        if read_type == "Read Coils":

            value_list = c.read_coils(regester_address)
            reg_status = ','.join(str(v) for v in value_list)
            print(reg_status)
            time_ = time.time()
            date = str(datetime.datetime.utcfromtimestamp(time_).strftime('%Y-%m-%d %H-%M-%S'))
            d.add_reg_status_data(date, reg_name, ip, regester_address, reg_status)
            time.sleep(samplig_time)

            if phone_message_status == 1:
                op.phone_notification(phone_number, range_min, range_max)

        if read_type == "Read Holding Regester":

            value_list = c.read_holding_registers(regester_address)
            reg_status = ','.join(str(v) for v in value_list)
            print(reg_status)
            print(type(reg_status))

            time_ = time.time()
            date = str(datetime.datetime.utcfromtimestamp(time_).strftime('%Y-%m-%d %H-%M-%S'))
            d.add_reg_status_data(date, reg_name, ip, regester_address, reg_status)
            time.sleep(samplig_time)

            if phone_message_status == 1:
                op.phone_notification(phone_number, range_min, range_max)

        if read_type == "Read Discrete Inputs":

            value_list = c.read_discrete_inputs(regester_address)
            reg_status = ','.join(str(v) for v in value_list)

            time_ = time.time()
            date = str(datetime.datetime.utcfromtimestamp(time_).strftime('%Y-%m-%d %H-%M-%S'))
            d.add_reg_status_data(date, reg_name, ip, regester_address, reg_status)
            time.sleep(samplig_time)

            if phone_message_status == 1:
                op.phone_notification(phone_number, range_min, range_max)

        if read_type == "Read Input Regester":

            value_list = c.read_input_registers(regester_address)
            reg_status = ','.join(str(v) for v in value_list)

            time_ = time.time()
            date = str(datetime.datetime.utcfromtimestamp(time_).strftime('%Y-%m-%d %H-%M-%S'))
            d.add_reg_status_data(date, reg_name, ip, regester_address, reg_status)
            time.sleep(samplig_time)

            if phone_message_status == 1:
                op.phone_notification(phone_number, range_min, range_max)

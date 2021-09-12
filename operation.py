from tkinter import messagebox
import threading
from settings import Variables
from database import data, return_data
import Modbus_Tcp as mtcp
from UI import App

rd = return_data()
d = data()
v = Variables()


def record_control_block(record_name):
    control = True
    data = rd.regester_name_return()
    try:
        if record_name:
            for i in data:
                a = ''.join(i)
                if a == record_name:
                    control = False
                if not control:
                    break
            if control:
                messagebox.showinfo(v.successful_message, v.successful_message)
            if not control:
                messagebox.showinfo(v.unsuccessful_message, "Regester name used before")
        else:
            messagebox.showinfo(v.unsuccessful_message, "Regester name used before")
    except:
        control = True
    return control


def data_tracking(reg_name, reading_type, host, port, reg_address, samplig_status, sampling_interval,
                  sampling_interval_unit, phone_number, phone_message_status, range_min, range_max):
    ##EKLENECEKLER
    ##İş parçacıklarının sıralı çalıştırılması.
    ##Bagımsız Çalışan İş parçacıklarının dışarıdan müdahale ile durdurulası
    server_list = []
    if samplig_status == 2:
        if sampling_interval_unit == "Second":
            sampling_time = sampling_interval
            server = threading.Thread(target=mtcp.tcp_listen_line,
                                      args=(
                                          reg_name, reading_type, reg_address, host, port, sampling_time, phone_number,
                                          phone_message_status, range_min, range_max))
            server_list.append(server)
            server.start()

        if sampling_interval_unit == "Minute":
            sampling_time = sampling_interval * 60
            server = threading.Thread(target=mtcp.tcp_listen_line,
                                      args=(
                                          reg_name, reading_type, reg_address, host, port, sampling_time, phone_number,
                                          phone_message_status, range_min, range_max))
            server_list.append(server)
            server.start()
        if sampling_interval_unit == "Hour":
            sampling_time = sampling_interval * 60 * 60
            server = threading.Thread(target=mtcp.tcp_listen_line,
                                      args=(
                                          reg_name, reading_type, reg_address, host, port, sampling_time, phone_number,
                                          phone_message_status, range_min, range_max))
            server_list.append(server)
            server.start()

        if sampling_interval_unit == "Day":
            sampling_time = sampling_interval * 60 * 60 * 24
            server = threading.Thread(target=mtcp.tcp_listen_line,
                                      args=(
                                          reg_name, reading_type, reg_address, host, port, sampling_time, phone_number,
                                          phone_message_status, range_min, range_max))
            server_list.append(server)
            server.start()

    if samplig_status == 1:
        sampling_time = 0
        server = threading.Thread(target=mtcp.tcp_listen_line,
                                  args=(reg_name, reading_type, reg_address, host, port, sampling_time, phone_number,
                                        phone_message_status, range_min, range_max))
        server_list.append(server)
        server.start()
        return server_list


def data_repording(report_select, reg_name, email, reading_period, reading_period_unit, range_min, range_max):
    ## report select == 1 ilse yalnızca veriler, 2 ise analizi yapılmış veriler raporlanacak
    if report_select == 1:
        if reading_period_unit == "Hour":
            repording_time = reading_period * 60 * 60
            ##Rapor olustur mail at
        if reading_period_unit == "Day":
            repording_time = reading_period * 60 * 60 * 24
            ##Rapor olustur mail at
    if report_select == 2:
        if reading_period_unit == "Hour":
            analiys(range_min, range_max)
            repording_time = reading_period * 60 * 60
            ##Rapor olustur mail at
        if reading_period_unit == "Day":
            analiys(range_min, range_max)
            repording_time = reading_period * 60 * 60 * 24
            ##Rapor olustur mail at


def analiys(range_min, range_max):
    #Okunan anlık verinin istenilen değerde olup olmadığının kontrulü yapılacak ve bool dönecek
    return True


def phone_notification(phone_number, range_min, range_max):
    analiys_status = analiys(range_min, range_max)
    if analiys_status == True:
        pass
        ##gsm modülüne git ve phone number a mesaj at
    if analiys_status == False:
        pass

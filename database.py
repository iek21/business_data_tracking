import sqlite3


class data(object):

    def __init__(self):
        self.con = sqlite3.connect("Register_Contact_Data.db")
        self.cursor = self.con.cursor()
        self.open = self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Register_Contact_Data(Regester_Name TEXT, Host INT, Reading_Type TEXT, Register_Address INT, Reporting_Period TEXT, Sampling_Interval TEXT, Range_Of_Word_Max INT, Range_Of_Word_Min INT, Email TEXT, Phone TEXT)")

    def add_data(self, Regester_Name, Host, Reading_Type, Register_Address, Reporting_Period, Sampling_Interval,
                 Range_Of_Word_Max, Range_Of_Word_Min, Email, Phone):
        self.cursor.execute(
            "INSERT INTO Register_Contact_Data (Regester_Name, Host, Reading_Type, Register_Address, Reporting_Period, Sampling_Interval, Range_Of_Word_Max, Range_Of_Word_Min, Email, Phone) VALUES (?,?,?,?,?,?,?,?,?,?) ",
            (
                Regester_Name, Host, Reading_Type, Register_Address, Reporting_Period, Sampling_Interval,
                Range_Of_Word_Max,
                Range_Of_Word_Min, Email, Phone))
        self.con.commit()

    def add_reg_status_data(self, date, reg_name, host, regester_address, reg_status):
        self.con_r = sqlite3.connect("Regester_Status.db")
        self.cursor_r = self.con_r.cursor()
        self.cursor_r.execute(
            "CREATE TABLE IF NOT EXISTS Regester_Status(Date TEXT, Regester_Name TEXT, Host TEXT, Register_Address INT,  Reg_Status TEXT)")
        self.con_r = sqlite3.connect('Regester_Status.db', check_same_thread=False)
        self.cursor_r.execute(
            "INSERT INTO Regester_Status(Date, Regester_Name, Host, Register_Address,  Reg_Status) VALUES (?,?,?,?,?) ",
            (date, reg_name, host, regester_address, reg_status))
        self.con_r.commit()


class return_data(data):

    def __init__(self):
        super().__init__()

    def regester_name_return(self):
        self.cursor.execute(("SELECT Regester_Name FROM Register_Contact_Data"))
        data = self.cursor.fetchall()
        self.con.commit()
        return data

import minimalmodbus


## Blok Modbus RTU Com Seçeneğine kırılım olarak bağlanacak
class ModbusRTU(object):

    def __init__(self, com, slave_id, baudrate, bytesize, stop_bit, timeout, parity):

        pb = self.parity(self, parity)

        self.instrumentA = minimalmodbus.Instrument(com, slave_id)  ##'/dev/ttyUSB1', 0
        self.instrumentA.serial.baudrate = baudrate
        self.instrumentA.serial.bytesize = bytesize
        self.instrumentA.serial.parity = pb
        self.instrumentA.serial.stopbits = stop_bit
        self.instrumentA.serial.timeout = timeout
        self.instrumentA.mode = minimalmodbus.MODE_RTU

    def parity(self, parity):

        pb = serial.PARITY_NONE
        if parity == "None":
            pb = serial.PARITY_NONE
        elif parity == "Odd":
            pb = serial.PARITY_ODD
        elif parity == "Even":
            pb = serial.PARITY_EVEN
        elif parity == "Mark":
            pb = serial.PARITY_MARK
        elif parity == "Space":
            pb = serial.PARITY_SPACE
        return pb

    def read_single_coil_function(self, register_address):

        try:
            read_register = self.instrumentA.read_bit(register_address, functioncode=1)
            read_status = True
        except IOError:
            read_register = False
            read_status = 0
        return read_register, read_status

    def read_discrete_inputs_function(self, register_address):

        try:
            read_register = self.instrumentA.read_bit(register_address, functioncode=2)
            read_status = True
        except IOError:
            read_register = False
            read_status = 0
        return read_register, read_status

    def read_holding_register_function(self, register_address, number_of_decimal):

        try:
            read_register = self.instrumentA.read_register(register_address, number_of_decimal, functioncode=3)
            read_status = True
        except IOError:
            read_register = False
            read_status = 0
        return read_register, read_status

    def read_inputs_register_function(self, register_address, number_of_decimal):

        try:
            read_register = self.instrumentA.read_register(register_address, number_of_decimal, functioncode=3)
            read_status = True
        except IOError:
            read_register = False
            read_status = 0
        return read_register, read_status

# read both left & right joycon flash dump
rspi_flash = None
lspi_flash = None
with open("controller.bin", 'rb') as rspi_flash_file:
    rspi_flash = rspi_flash_file.read()
    
with open("controller.bin", 'rb') as lspi_flash_file:
    lspi_flash = lspi_flash_file.read()
    


class FlashMemory:
    def __init__(self, spi_flash_memory_data=None, size=0x80000):
        if spi_flash_memory_data is None:
            self.data = size * [0x00]
        else:
            if len(spi_flash_memory_data) != size:
                raise ValueError(f'Given data size {len(spi_flash_memory_data)} does not match size {size}.')
            if isinstance(spi_flash_memory_data, bytes):
                spi_flash_memory_data = list(spi_flash_memory_data)
                lspi_flash_memory_data = list(lspi_flash)
                rspi_flash_memory_data = list(rspi_flash)
            self.data = spi_flash_memory_data
            self.ldata = lspi_flash_memory_data
            self.rdata = rspi_flash_memory_data

    def __getitem__(self, item):
        return self.data[item]

    def get_factory_l_stick_calibration(self):
        """
        :returns 9 left stick factory calibration bytes
        """
        #print("Factory L")
        #print((self.ldata[0x603D:0x6046]))
        return self.ldata[0x603D:0x6046]

    def get_factory_r_stick_calibration(self):
        """
        :returns 9 right stick factory calibration bytes
        """
        #print("Factory R")
        #print((self.rdata[0x6046:0x604F]))
        return self.rdata[0x6046:0x604F]

    def get_user_l_stick_calibration(self):
        """
        :returns 9 left stick user calibration bytes if the data is available, otherwise None
        """
        # check if calibration data is available:
        if self.ldata[0x8010] == 0xB2 and self.ldata[0x8011] == 0xA1:
            #print("User L")
            #print((self.ldata[0x8012:0x801B]))
            return self.ldata[0x8012:0x801B]
        else:
            return None

    def get_user_r_stick_calibration(self):
        """
        :returns 9 right stick user calibration bytes if the data is available, otherwise None
        """
        # check if calibration data is available:
        if self.rdata[0x801B] == 0xB2 and self.rdata[0x801C] == 0xA1:
            #print("User R")
            #print((self.rdata[0x801D:0x8026]))
            return self.rdata[0x801D:0x8026]
        else:
            return None


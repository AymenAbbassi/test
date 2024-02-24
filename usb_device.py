import usb.core

class USBDevice:

    def __init__(self, idVendor, idProduct) -> None:
        """Run lsusb to detect usb devices connected. Then run lsusb -D /dev/bus/usb/{BUSNUMBER}/{DEVICENUMBER} and replace BUSNUMBER and DEVICENUMBER
        with the devices number
        """

        self.idVendor = idVendor
        self.idProduct = idProduct

        try:
            self.device = usb.core.find(find_all=True, idVendor=self.idVendor, idProduct=self.idProduct)
        except:
            print("No backend available")
    
    def read() -> None:
        pass

        
            

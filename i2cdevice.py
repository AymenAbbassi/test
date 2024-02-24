import abc
from abc import ABC
import time 
from typing import Any
from smbus2 import SMBus

class I2CDevice(ABC):

    device = "I2C Device"

    def __init__(self, bus: int, addr: int) -> None:
        self.address = addr
        self.bus = SMBus(bus)
        self.bus.enable_pec(True)
    
    @classmethod
    def __str__(cls) -> str:
        return cls.device
    
    @abc.abstractclassmethod
    def write(self, reg: int, data: list) -> float | None:

        assert len(data) < 32
        try:
            start = time.perf_counter()
            self.bus.write_i2c_block_data(self.address, reg, data)
            stop = time.perf_counter()
            return stop - start
        except:
            print(f"Could not send {data} to register {reg} of address {self.address}")
            return

    @abc.abstractclassmethod
    def read(self, reg: int, bytes: int) -> tuple[float, list[int]] | None:

        assert bytes < 32
        try:
            start = time.perf_counter()
            data: list = self.bus.read_i2c_block_data(self.address, reg, bytes)
            stop = time.perf_counter()
            return (stop - start, data)
        except:
            print(f"Could not read {bytes} of data from register {reg} of address {self.address}")
            return
    
    

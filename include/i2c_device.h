#ifndef I2C_DEVICE
#define I2C_DEVICE
#include "smbus.h"
#include <cstdint>
#include "../../../../../usr/include/x86_64-linux-gnu/sys/types.h"

class I2CDevice {
    private:
        char filename[20];
    public:
        struct {
            unsigned long* i2c_peripheral;
            int file;
            int adapter_nr;
            u_char reg;
        };

        I2CDevice(unsigned long addr, int adapter_nmb, const u_char reg);
        void read_file();
        __s32* open_file();
    
};

#endif
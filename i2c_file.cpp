#include <stdio.h>
#include <iostream>
#include <linux/i2c-dev.h>
#include <linux/i2c.h>
#include <sys/ioctl.h>
#include <sys/fcntl.h>
#include "include/smbus.h"
#include "include/i2c_device.h"
#include <thread>

#define I2C_ADDRESS 0x40


class I2CDevice {

    private:
        char filename[20];
             
    public:
        struct {
            unsigned long* i2c_peripheral;
            int file;
            int adapter_nr;
            u_char reg;
        } configs;


        I2CDevice::I2CDevice(unsigned long addr, int adapter_nmb, const u_char reg) {
            const uint8_t new_file = open(filename, O_RDWR);
            configs = {&addr, new_file, adapter_nmb, reg};
            snprintf(filename, 19, "/dev/i2c-%d", configs.adapter_nr);
        }
            

        __s32* I2CDevice::open_file() {
            if (configs.file < 0) {
                exit(1);
            }
            if (ioctl(configs.file, *configs.i2c_peripheral, I2C_ADDRESS) < 0) {
                exit(1);
            }    

            __s32 res = i2c_smbus_read_word_data(configs.file, configs.reg);
            if (res < 0) {
                return 0;
            } else {
                return &res;
            }
        }

};

int main(int argc, char *argv[]) {
    
    return 0;
}


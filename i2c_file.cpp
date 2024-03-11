#include <stdio.h>
#include <iostream>
#include <linux/i2c-dev.h>
#include <linux/i2c.h>
#include <sys/ioctl.h>
#include <sys/fcntl.h>
#include <smbus.h>

#define I2C_ADDRESS 0x40

struct {
    
};

class I2CDevice {

    private:
        const uint8_t* i2c_peripheral {};

    public:

        I2CDevice(uint8_t addr): i2c_peripheral(&addr) {} 
        
        void read_data() {}
        void open_file() {

            int file;
            int adapter_nr = 2; 
            char filename[20];

            snprintf(filename, 19, "/dev/i2c-%d", adapter_nr);
            file = open(filename, O_RDWR);
            if (file < 0) {
                exit(1);
            }

            if (ioctl(file, *i2c_peripheral, I2C_ADDRESS) < 0) {
            
                exit(1);
            }    
            const u_char reg = 0x10;
            signed int res;
            char buf[10];

            res = i2c_smbus_read_word_data(file, reg);
            if (res < 0) {

            } else {
                printf("%d\n", res);
            }
            buf[0] = reg;
            buf[1] = 0x43;
            buf[2] = 0x65;
        }
};

int main(int argc, char *argv[]) {
    return 0;
}


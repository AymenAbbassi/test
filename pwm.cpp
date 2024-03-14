#include <stdio.h>
#include <iostream>
#include <string.h>
#include <fcntl.h>
#include <fstream>
#include <unistd.h>


class PWM {

    std::ofstream _file;
    private:
        char _chip[30];
        unsigned long _period;
    public:

        PWM(char chip[15], unsigned long period) {
            _file.open("/sys/class/pwm/pwm0/polarity");
            if(!_file) {
                _file.close();
                char* export_path;
                snprintf(export_path, 25, "/sys/class/pwm/%s/export", chip);
                _file.open(export_path, std::ios::out);
                if(!_file) {
                    std::cout << "Error exporting file" << std::endl;
                }
                _file << 0;
                _file.close();

                sleep(0.2);

                _period = period;
                _file.open("/sys/class/pwm/pwm0/period", std::ios::out);
                _file << _period;
                _file.close();

                _file.open("/sys/class/pwm/pwm0/polarity", std::ios::out);
                _file << "normal";
                _file.close();
            }
            _file.close();
        }
    
        void _set_duty_cycle(double cycle) {
            if(cycle > 1.0 || cycle < 0.0) {
                std::cout << "Duty cycle exceeded maximum" << std::endl;
            }
            cycle *= _period;

            _file.open("/sys/class/pwm/pwm0/duty_cycle", std::ios::out);
            _file << cycle;
            _file.close();
        } 

        void stop() {
            _file.open("/sys/class/pwm/pwm0/duty_cycle", std::ios::out);
            _file << 0;
            _file.close();
        } 

        void set_period(unsigned long period) {
            _period = period;
            _file.open("/sys/class/pwm/pwm0/period", std::ios::out);
            _file << _period;
            _file.close();
        }

        void set_polarity(std::string polarity) {
            _file.open("/sys/class/pwm/pwm0/polarity", std::ios::out);
            _file << polarity;
            _file.close();
        }
};


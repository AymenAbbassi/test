#!/etc/bin/env python3

from typing import Any
from inputs import get_gamepad, UnpluggedError
from threading import Thread
from math import pow
from time import sleep
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-p", "--print", help="Print the values from the controller")

args = parser.parse_args()

class XboxController:

    controller: str = "Xbox One Controller"

    def __init__(self, deadzone: float = 0.1) -> None:

        self.deadzone = deadzone
        self.MAX_TRIG_VAL = pow(2, 8)
        self.MAX_JOY_VAL = pow(2, 15)
        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self.controller_thread = Thread(target=self.monitor_inputs, daemon=True)
        self.controller_thread.start()

    @classmethod
    def __str__(cls) -> str:
        return cls.controller

    def monitor_inputs(self) -> None:
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = -event.state / self.MAX_JOY_VAL if abs(event.state / self.MAX_JOY_VAL) >= self.deadzone else 0
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / self.MAX_JOY_VAL if abs(event.state / self.MAX_JOY_VAL) >= self.deadzone else 0
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = -event.state / self.MAX_JOY_VAL if abs(event.state / self.MAX_JOY_VAL) >= self.deadzone else 0
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / self.MAX_JOY_VAL if abs(event.state / self.MAX_JOY_VAL) >= self.deadzone else 0
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / self.MAX_TRIG_VAL 
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / self.MAX_TRIG_VAL 
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_WEST':
                    self.Y = event.state 
                elif event.code == 'BTN_NORTH':
                    self.X = event.state 
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'ABS_HAT0X':
                    self.LeftDPad = -event.state if event.state == -1 else 0
                    self.RightDPad = event.state if event.state == 1 else 0
                elif event.code == 'ABS_HAT0Y':
                    self.UpDPad =  -event.state if event.state == -1 else 0
                    self.DownDPad = event.state if event.state == 1 else 0
                
    @property
    def joysticks(self) -> list[float, float, float, float]:
        return [self.LeftJoystickX, self.LeftJoystickY, self.RightJoystickX, self.RightJoystickY]
    
    @property
    def buttons(self) -> list[bool, bool, bool, bool]:
        return [self.A, self.B, self.X, self.Y]
    
    @property
    def triggers(self) -> list[float, float]:
        return [self.LeftTrigger, self.RightTrigger]
    
    @property
    def bumpers(self) -> list[bool, bool]:
        return [self.LeftBumper, self.RightBumper]
    
    @property
    def d_pads(self) -> list[bool, bool, bool, bool]:
        return [self.UpDPad, self.DownDPad, self.LeftDPad, self.RightDPad]

    def print_values(self) -> None:
        print("Xbox Controller")
        print("    joysticks:")
        print(f"       leftx: {self.joysticks[0]}")    
        print(f"       lefty: {self.joysticks[1]}")    
        print(f"       rightx: {self.joysticks[2]}")    
        print(f"       righty: {self.joysticks[3]}")
        print("    triggers:")
        print(f"       lefttrigger: {self.triggers[0]}")    
        print(f"       righttrigger: {self.triggers[1]}")
        print("    bumpers:")
        print(f"       leftbumper: {self.bumpers[0]}")    
        print(f"       rightbumper: {self.bumpers[1]}")
        print("    buttons:")
        print(f"       a: {self.buttons[0]}")    
        print(f"       b: {self.buttons[1]}")    
        print(f"       x: {self.buttons[2]}")    
        print(f"       y: {self.buttons[3]}")
        print("    d_pad:")
        print(f"       up_dpad: {self.d_pads[0]}")    
        print(f"       down_dpad: {self.d_pads[1]}")    
        print(f"       left_dpad: {self.d_pads[2]}")    
        print(f"       right_dpad: {self.d_pads[3]}")

def main() -> None:
    xbox_controller = XboxController(0.2)
    if args.print == "print":
        while True:
            xbox_controller.print_values()
            sleep(0.1)

if __name__ == "__main__":
    main()
    
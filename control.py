from simple_pid import PID
from yaml import safe_load
from time import sleep
from xbox_controller import XboxController

class PIDController:

    def __init__(self, name: str) -> None:
        self.name = name
        self.pid_controller = PID()
        self.pid_controller.Kp = 0 
        self.pid_controller.Ki = 0 
        self.pid_controller.Kd = 0
        self.pid_controller.setpoint = 0
        self.pid_controller.sample_time = 0
              
    def __call__(self, input: float) -> float:
        """Return the output of the PID controller"""
        #print(f"KP: {self.pid_controller.Kp} KI: {self.pid_controller.Ki}, KD: {self.pid_controller.Kd}, Update: {self.pid_controller.sample_time}, Setpoint: {self.pid_controller.setpoint}")
        return self.pid_controller.__call__(input)

    @property.setter
    def yaml_file(self) -> list[float, float, float, float] | None:
        """Get the yaml file configuration for this PID controller"""
        try:
            with open(r"pid\pid_configs.yaml", "r") as f:
                yaml_file = safe_load(f)
            self.pid_controller.Kp = yaml_file[f"{self.name}"]["KP"], 
            self.pid_controller.Ki = yaml_file[f"{self.name}"]["KI"], 
            self.pid_controller.Kd = yaml_file[f"{self.name}"]["KD"], 
            self.pid_controller.setpoint = yaml_file[f"{self.name}"]["Setpoint"], 
            self.pid_controller.sample_time = yaml_file[f"{self.name}"]["Update_Rate"]
        except KeyError:
            print("The wrong key was entered")
            return

    def reset(self) -> None:
        """Reset the PID controller to zero and clear last calculations"""
        self.pid_controller.reset()
    
    def set_setpoint(self, setpoint: float) -> None:
        """Set the setpoint the PID controller will target"""
        self.pid_controller.setpoint = setpoint

def main() -> None:
    pid1 = PIDController("PID1")
    xbox_controller = XboxController(0.2)
    while True:
        print(pid1(xbox_controller.joysticks[0]))
        sleep(0.1)

if __name__ == "__main__":
    main()
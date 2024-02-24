from simple_pid import PID
import os
import yaml

class PIDController:

    def __init__(self, name: str) -> None:
        self.name = name
        self.yaml_file_configs = self.get_yaml_file()
        self.pid_controller = PID()
        self.pid_controller.Kp = self.yaml_file_configs[0], 
        self.pid_controller.Ki = self.yaml_file_configs[1], 
        self.pid_controller.Kd = self.yaml_file_configs[2],
        self.pid_controller.setpoint = self.yaml_file_configs[3]
        self.pid_controller.sample_time = self.yaml_file_configs[4]
          
    def __call__(self, input: float) -> float:
        """Return the output of the PID controller"""
        return self.pid_controller.__call__(input)


    def get_yaml_file(self) -> list[float, float, float, float] | None:
        """Get the yaml file configuration for this PID controller"""
        try:
            with open(r"pid\pid_configs.yaml", "r") as f:
                yaml_file = yaml.safe_load(f)
            return [yaml_file[f"{self.name}"]["KP"], yaml_file[f"{self.name}"]["KI"], yaml_file[f"{self.name}"]["KD"], yaml_file[f"{self.name}"]["Setpoint"], yaml_file[f"{self.name}"]["Update_Rate"]]
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

if __name__ == "__main__":
    main()
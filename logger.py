from datetime import datetime
from random import randint
from time import sleep
from typing import Dict

def log(message: str, *args) -> None:
    time: datetime = datetime.now()
    for arg in args:
        match arg:
            case "warn":
                print(f"\033[93m [{time}] [WARN] {message}\033[93m")
            case "err":
                print(f"\033[91m [{time}] [ERR] {message}\033[91m")
            case "std":
                print(f"\033[0m [{time}] {message} \033[0m")
            case "good":
                print(f"\033[0m\033[92m [{time}] {message} \033[92m\033[0m")
            case "general":
                print(f"\033[1m\033[0m\033[4m [{time}] {message} \033[4m\033[1m\033[0m")
            case _:
                raise ValueError("\033[91m An invalid type was entered \033[91m \n")

if __name__ == "__main__":
    while True:
        random_number: int = randint(1, 5)
        match random_number:
            case 1:
                log("hello", "warning")
            case 2:
                log("another message", "error")
            case 3:
                log("another file", "standard")
            case 4:
                log("This is a good message", "good")
            case 5:
                log("This is a general message", "general")
        sleep(0.1)



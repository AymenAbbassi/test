from datetime import datetime
from random import randint
from time import sleep
from typing import Dict
import enum

class Colors:
    ERROR = "\x1B[38;5;124m"
    FATAL_ERROR ="\x1B[38;5;52m"
    WARNING = "\x1B[38;5;172m"
    GOOD = "\x1B[38;5;46m"
    CLEAR = "\033[0m"

def log(message: str, *args) -> None:
    time: datetime = datetime.now()
    for arg in args:
        match arg:
            case "warn":
                print(f"{Colors.CLEAR}{Colors.WARNING}[{time}] [WARN] {message}{Colors.WARNING}{Colors.CLEAR}")
            case "err":
                print(f"{Colors.CLEAR}{Colors.ERROR}[{time}] [ERR] {message}{Colors.ERROR}{Colors.CLEAR}")
            case "std":
                print(f"{Colors.CLEAR}[{time}] {message}{Colors.CLEAR}")
            case "fatal":
                print(f"{Colors.CLEAR}{Colors.FATAL_ERROR}[{time}] [FATAL] {message}{Colors.FATAL_ERROR}{Colors.CLEAR}")
            case "good":
                print(f"{Colors.CLEAR}{Colors.GOOD}[{time}] {message}{Colors.GOOD}{Colors.CLEAR}")
            case "general":
                print(f"{Colors.CLEAR}[{time}] {message}{Colors.CLEAR}")
            case _:
                raise ValueError("\033[91m An invalid type was entered \033[91m \n")




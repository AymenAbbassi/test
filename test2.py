import json
from threading import Thread
from time import sleep
from test3 import print_file
from random import randint
import test6

def print_file2() -> None:
    with open("/home/aymen/Desktop/test/data1.json", "r") as f:
        data = json.load(f)  

    ## Working with buffered content
    data["motor speed"] = randint(0, 100) 
    data["speed"] = randint(0, 100)
    data["altitude"] = randint(0, 100)

    with open("/home/aymen/Desktop/test/data1.json", "w+") as f:
        f.write(json.dumps(data))

    sleep(0.03)

def main() -> None:
    while True:
        print_file2()
        sleep(0.1)

if __name__ == "__main__":
    main()
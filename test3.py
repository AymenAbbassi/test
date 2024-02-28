from time import sleep
import json
import test6

def print_file() -> None:
    try:
        with open("/home/aymen/Desktop/test/data1.json", "r") as file:
            print(json.load(file), end="\r")
            sleep(0.1)
    except:
        print("an exception occured")

def main() -> None:
    while True:
        print_file()

if __name__ == "__main__":
    main()
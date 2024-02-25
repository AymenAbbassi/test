import json
import random
from time import sleep

def json_writer() -> None:
    for i in range(20):
        with open("data1.json", "w") as f:
            numbers: dict = {"altitude": random.randint(0, 2000), "motor speed": random.randint(0, 2000), "speed": random.randint(0, 2000)}
            # data = json.load(f)
            # data["altitude"] = random.randint(0, 2000)
            json.dump(numbers, f)
        sleep(1)

def main() -> None:
    json_writer()

if __name__ == "__main__":
    main()
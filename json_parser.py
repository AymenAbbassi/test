import json
from threading import Thread
import os
from time import sleep 
import test1

class JSONParser:

    name = "JSONParser"

    def __init__(self, file_path: str) -> None:

        self.file = None
        if not os.path.exists(file_path):
            print(f"The JSON file {file_path} does not exist")

        self.file_path = file_path

        self.json_thread = Thread(target=self.monitor_json_data)
        self.json_thread.start()

    @classmethod
    def __str__(cls) -> str:
        return cls.name
    
    def monitor_json_data(self) -> None:
        with open(self.file_path, "r") as f:
            while True:
                self.file = json.load(f)

    def request_json_stream(self) -> dict:
        return self.file
    
def main() -> None:
    parser = JSONParser("data1.json")
    test1.json_writer()
    while True:
        #print(parser.request_json_stream())
        sleep(0.1)

if __name__ == "__main__":
    main()

import json
from threading import Thread
import os 

class JSONParser:

    name = "JSONParser"

    def __init__(self, file_path: str) -> None:

        self.file = None
        if not os.path.exists(file_path):
            print(f"The JSON file {file_path} does not exist")

        self.file_path = file_path

        self.json_thread = Thread(target=self.monitor_json_data, daemon=True)
        self.json_thread.start()

    @classmethod
    def __str__(cls) -> str:
        return cls.name
    
    def monitor_json_data(self) -> None:
        while True:
            self.file = json.load(self.file)

    def request() -> None:
        pass
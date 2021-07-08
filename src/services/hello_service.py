from src.models.hello import HelloModel
from datetime import datetime
import os
import time

class HelloService:

    def __init__(self):
        self.file_name = 'tasks.log'
        
    def send_hello(self, model: HelloModel):
        time.sleep(20)
        file_path = f"{os.getcwd()}/{self.file_name}"
        with open(file_path, 'a') as file:
            file.write(f' Task Hello: sending message "{model.message}" to "{model.name}" at {datetime.now().isoformat()} ')
            file.write("\n")
import os
import json

from controller.logs import LogManager

class CredentialManager:
    
    def __init__(self) -> None:
        self.file = os.path.join(os.getcwd(), "credentials.json")
        self.lm = LogManager()
        self.logger = self.lm.create_logger(f'credential.py')
    
    def get(self) -> dict:
        
        self.logger.info("Accessing the credentials.")
        with open(self.file, "r") as f:
            data = json.load(f)
        self.logger.info("Credentials successfully retrieved.")
        
        return data
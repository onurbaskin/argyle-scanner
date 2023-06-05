from controller.keyvault import KeyVault
from controller.credential import CredentialManager
from scanner.upwork_scanner import UpWorkScanner
from dotenv import find_dotenv, load_dotenv


if __name__ == "__main__":
    
    if find_dotenv:
        load_dotenv()
        
    cm = CredentialManager()
    data = cm.get()
    
    kv = KeyVault()
    
    upwork = UpWorkScanner()
    
    for user in data:
        upwork.upwork_scanner(
            data[user].get("username"),
            data[user].get("password"),
            data[user].get("secret"),
            kv.get_secret("URL")
        )

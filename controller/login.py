from playwright.sync_api import Page
from controller.keyvault import KeyVault
from controller.logs import LogManager


class LoginController:
    
    def __init__(self, username, password, secret, url) -> None:
        self.kv = KeyVault()
        self.lm = LogManager()
        self.logger = self.lm.create_logger(f'login.py')
        
        self.USERNAME = username
        self.PASSWORD = password
        self.SECRET = secret
        self.URL = url
        
    
    def login(self, page:Page) -> None:
        self.logger.info(f"Visiting the page: {self.URL}")
        page.goto(self.URL)
        
        self.logger.info(f"Username injected.")
        page.fill('#login_username', self.USERNAME)
        page.click('#login_password_continue')
        
        self.logger.info(f"Password injected.")
        page.fill('#login_password', self.PASSWORD)
        page.click('#login_control_continue')
        
        try:
            self.logger.info(f"Secret requested.")
            try:
                page.wait_for_selector("text=Let's make sure it's you", timeout=5000)
            except TimeoutError as e:
                raise f"An Exception Occurred: {e}"
         
            self.logger.info(f"Secret injected.")
            page.fill('#login_answer', self.SECRET)
            page.click('#login_control_continue')
        except TimeoutError as e:
            self.logger.error(f"An Exception Occurred: {e}")
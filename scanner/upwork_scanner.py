import os
import json

from playwright.sync_api import sync_playwright, Page
from user_agent import generate_user_agent

from controller.logs import LogManager
from controller.login import LoginController
from model.items import User, MainPage, ProfilePage


class UpWorkScanner:
    
    def __init__(self) -> None:
        self.output = os.path.join(os.getcwd(), "data/result.json")
        self.company = "UpWork"
        self.lm = LogManager()
        self.logger = self.lm.create_logger(f'upwork_scanner.py')
    
    
    def scan_page(self, user: User, page: Page) -> None:
        main = MainPage(user)
        main.scan(page)
        profile = ProfilePage(user)
        profile.scan(page)
    
    
    def upwork_scanner(self, username, password, secret, url) -> None:
        with sync_playwright() as p:
            
            # slow_mo parameter initiated to prevent catpcha wall. 
            browser = p.chromium.launch(headless=True, slow_mo=100)
            
            # Random User-Agent switching for each run.
            context = browser.new_context(user_agent=generate_user_agent())
            
            # Initiate a new page instance
            page = context.new_page()

            lc = LoginController(username, password, secret, url)
            
            lc.login(page)
            
            page.goto("https://www.upwork.com/nx/find-work/best-matches")

            user = User()
            self.scan_page(user, page)

            with open(self.output, 'w') as f:
                json.dump(user.dict(), f)

            browser.close()

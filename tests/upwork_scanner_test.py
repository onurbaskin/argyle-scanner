from controller.credential import CredentialManager
from controller.keyvault import KeyVault
from controller.login import LoginController
from user_agent import generate_user_agent


def test_login(browser):
    
    kv = KeyVault()
    
    cm = CredentialManager()
    data = cm.get()
    
    context = browser.new_context(user_agent=generate_user_agent())
    
    page = context.new_page()
    
    lc = LoginController(
        data["0001"].username,
        data["0001"].password,
        data["0001"].secret,
        kv.get_secret("URL")
    )
    
    lc.login(page)
    
    assert page.title() == 'My Job Feed'
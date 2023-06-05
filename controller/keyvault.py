""" Example Microsoft Azure Key Vault Secret Retriever.
    Fallbacks to .env file values.
"""
import os
from azure.identity import DefaultAzureCredential
from controller.logs import LogManager

class KeyVault:
    
    def __init__(self) -> None:
        self.lm = LogManager()
        self.logger = self.lm.create_logger("keyvault.py")
    
    def get_secret(self, requested_secret_name, key_vault_name = os.getenv("KEY_VAULT"), credential = DefaultAzureCredential()) -> str:
        """ Takes the key_vault_name variable from environment, credential value from
            Azure Key Vault integration to Azure App Service to request the secret
            from Azure Key Vault.
        
        Args:
            requested_secret_name (str): The secret stored in Azure Key Vault
            key_vault_name (str, optional): Azure Key Vault Instance. Defaults to os.getenv("KEY_VAULT").
            credential (instance, optional): Environment or Azure CLI credential information.
            Defaults to DefaultAzureCredential().

        Returns:
            str: Retrieved secret's value.
        """

        try:
            # I COMMENTED OUT THE BELOW CODE BLOCK SINCE THIS CODE CHALLENGE DOESN'T HAVE A KEYVAULT INSTANCE I CAN CONNECT TO.
            # THE PURPOSE OF THE CODE BLOCK IS JUST TO SHOW AN ALTERNATIVE TO DOTENV.
            # IN PRODUCTION, IN ANY CLOUD PROVIDER (AWS, GCP, AZURE, ETC.), A WRAPPER LIKE THIS SAVES TIME.
            """ 
            self.logger.info(f"Retrieving {requested_secret_name} value from the environment.")
            client = SecretClient(vault_url=f"https://{key_vault_name}.vault.azure.net/", credential=credential)
            retrieved_secret = client.get_secret(requested_secret_name)
            self.logger.info(f"Retrieved the secret {requested_secret_name} from {key_vault_name}.")
            
            return retrieved_secret.value
            """
            return os.getenv(requested_secret_name)
        
        except Exception as error_message:
            self.logger.info(f"Couldn't retrieve the secret {requested_secret_name} from the Key Vault. Error message: {error_message}")
            
            # FALLBACK TO DOTENV, IN CASE OF KEYVAULT ACCESS ISSUES.
            try:
                return os.getenv(requested_secret_name)
            
            except ValueError as error_message:
                self.logger.info(f"Couldn't retrieve the secret {requested_secret_name} from the Key Vault. Error message: {error_message}")
                return None
        
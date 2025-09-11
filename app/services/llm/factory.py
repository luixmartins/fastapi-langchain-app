import os 
from dotenv import load_dotenv 

load_dotenv()

from langchain.chat_models import init_chat_model 


class ChatModelFactory: 
    def __init__(
        self, 
        model_name: str = 'mistral-large-latest', 
        model_provider='mistralai'
    ): 
        self.model_name = model_name 
        self.model_provider = model_provider 
    
    def init_model(self): 
        return init_chat_model(
            "mistral-large-latest", 
            model_provider="mistralai"
        )
from app.core.settings import settings 

from langchain.chat_models import init_chat_model 

class ChatModelFactory: 
    def __init__(
        self, 
        model_name: str = 'mistral-large-latest', 
        model_provider='mistralai'
    ): 
        self.model_name = model_name 
        self.model_provider = model_provider 
        self.api_key = settings.MISTRAL_API_KEY
    
    def init_model(self): 
        return init_chat_model(
            "mistral-large-latest", 
            model_provider="mistralai", 
            model_kwargs={"api_key": self.api_key} 
        )
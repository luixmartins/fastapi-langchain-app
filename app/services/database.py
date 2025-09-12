from langchain_community.utilities import SQLDatabase
from app.core.settings import settings

DATABASE_URL = (
    f"mysql+mysqlconnector://{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

class DatabaseService: 
    def __init__(self, DATABASE_URL=DATABASE_URL): 
        self.db = SQLDatabase.from_uri(DATABASE_URL)
        
    def get_db(self): 
        return self.db 
    
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from core.settings import settings 
from api.routes.chatbot import router as chatbot_router 

app = FastAPI(
    title="Chatbot with LangChain and FastAPI", 
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot_router, prefix="/chatbot", tags=["chatbot"])


@app.get('/')
def root(): 
    return {"message": settings.MODEL_NAME}
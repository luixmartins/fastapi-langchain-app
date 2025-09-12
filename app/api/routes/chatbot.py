from fastapi import APIRouter

from app.models.schemas import QueryRequest
from app.services.llm.chains import ChainFactory 

router = APIRouter(
    tags=["chatbot"],
)

@router.get('/test')
async def test_endpoint(): 
    return {"message": "Chatbot endpoint is working!"} 

@router.post('/create_query')
async def create_query_endpoint(request: QueryRequest): 
    question = request.question
    
    factory = ChainFactory() 
    try: 
        response = factory.write_query(question)
    except Exception as e: 
        return {"error": str(e)}
    
    
    return {"question": response, "message": "Query received successfully!"}    

@router.post('/chat')
async def chat_endpoint(request: QueryRequest): 
    question = request.question
    
    factory = ChainFactory() 
    try: 
        state = factory.run_chain(question)
    
    except Exception as e: 
        return {"error": str(e)}
    
    return {
        "Answer:": state['answer']
        #"question": state['question'], 
        #"query": state['query'], 
        #"result": state['result'], 
        #"answer": state['answer'],
        #"message": "Chat processed successfully!"
    }
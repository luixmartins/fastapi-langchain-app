from fastapi import APIRouter

router = APIRouter(
    tags=["chatbot"],
)

@router.get('/test')
async def test_endpoint(): 
    return {"message": "Chatbot endpoint is working!"} 
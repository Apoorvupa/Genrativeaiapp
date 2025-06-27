# # # app/chat_api.py
# # from fastapi import APIRouter
# # from pydantic import BaseModel
# # from app.llm_model import generate_llm_response

# # router = APIRouter()

# # class ChatRequest(BaseModel):
# #     prompt: str

# # @router.post("/chat")
# # async def chat_with_llm(request: ChatRequest):
# #     response_text = generate_llm_response(request.prompt)
# #     return {"response": response_text}



# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.database import get_db  # ✅ ensure correct import path
# from app.models import ChatMessage
# from app.llm_model import generate_llm_response

# router = APIRouter()

# @router.post("/chat")
# def chat(prompt: str, db: Session = Depends(get_db)):
#     # ✅ Save user message
#     user_msg = ChatMessage(sender="user", message=prompt)
#     db.add(user_msg)

#     # ✅ Generate bot response using LLM
#     response = generate_llm_response(prompt)

#     # ✅ Save bot message
#     bot_msg = ChatMessage(sender="bot", message=response)
#     db.add(bot_msg)

#     # ✅ Commit both entries to database
#     db.commit()

#     return {"response": response}


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel  # ✅ Add this
from app.database import get_db
from app.models import ChatMessage
from app.llm_model import generate_llm_response

router = APIRouter()

# ✅ Define request body schema
class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    # ✅ Save user message
    user_msg = ChatMessage(sender="user", message=request.prompt)
    db.add(user_msg)

    # ✅ Generate bot response using LLM
    response = generate_llm_response(request.prompt)

    # ✅ Save bot message
    bot_msg = ChatMessage(sender="bot", message=response)
    db.add(bot_msg)

    db.commit()

    return {"response": response}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router as pdf_router
from app.chat_api import router as chat_router

# ✅ Import for DB table creation
from app.models import Base
from app.database import engine

# ✅ Create all tables at startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pdf_router)
app.include_router(chat_router)

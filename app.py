from fastapi import FastAPI, Depends, Request, Form, status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

app.get('/')
async def home(req : Request, db : Session = Depends(get_db)):
    return ""



from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import team

models.Base.metadata.create_all(bind=engine)
 
app = FastAPI()

app.include_router(team.router, prefix="/team", tags=["team"])

@app.get("/")
def root():
    return {"message": "Добро пожаловать на сайт для управления командами!"}
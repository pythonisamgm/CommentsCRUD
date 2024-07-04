from fastapi import FastAPI, Depends, HTTPException
from core import comments_models
from core.comments_database import engine
from routes import comments_routes
from routes.comments_routes import router

app = FastAPI()

app.include_router(router, prefix="/api")
comments_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def get_comment():
    return "hola, mundo"
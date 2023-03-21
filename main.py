from fastapi import FastAPI
from db import models
from db.database import engine
from router import user

app = FastAPI()
app.include_router(user.router)

@app.get('/')
def index():
    return {"message": "index"}

models.Base.metadata.create_all(engine)

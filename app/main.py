from fastapi import FastAPI
from . import models
from .database import engine
from .routers import recipe, user, auth, review, foodContent

models.Base.metadata.create_all(bind = engine)

app = FastAPI() 

app.include_router(recipe.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(review.router) 
app.include_router(foodContent.router)

@app.get("/") 
def root():
    return {"message": "Hello World"}
# Import Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

# Activate Router
router = APIRouter(
    prefix = "/review",
    tags = ['Review']
)

# Get All Reviews
@router.get("/", response_model = List[schemas.ReviewBase])
def get_review(db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    reviews = db.query(models.Review).all()
    return reviews
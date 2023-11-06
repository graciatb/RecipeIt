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

# Create Review
@router.post("/{recipe_id}", status_code = status.HTTP_201_CREATED, response_model = schemas.ReviewBase)
def create_review(recipe_id: int, review: schemas.ReviewBase, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
   if not db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first():
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Recipe with id {recipe_id} doesn't exist")
   new_review = models.Review(recipe_id = recipe_id, user_id = current_user.id,**review.model_dump())
   db.add(new_review)
   db.commit()
   db.refresh(new_review)
   return new_review

# Get Reviews by User Id
@router.get("/user/{user_id}")
def get_review_by_user_id(user_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    review = db.query(models.Review).filter(models.Review.user_id == user_id).all()
    if not review:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id {user_id} haven't written any reviews")
    return review

# Get Reviews by Recipe Id
@router.get("/recipe/{recipe_id}")
def get_review_by_recipe_id(user_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    review = db.query(models.Review).filter(models.Review.user_id == user_id).all()
    if not review:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Recipe with id {id} have no review")
    return review


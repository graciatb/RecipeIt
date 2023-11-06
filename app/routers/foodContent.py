# Import Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

# Activate Router
router = APIRouter (
    prefix = "/content",
    tags = ['Content']
)

# Get All Food Content
@router.get("/", response_model = List[schemas.FoodContentBase])
def get_contents(db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    contents = db.query(models.FoodContent).all()
    return contents

# Create Content
@router.post("/", status_code = status.HTTP_201_CREATED, response_model = schemas.FoodContent)
def create_content(content: schemas.ContentCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
   new_content = models.FoodContent(owner_id = current_user.id,**content.model_dump())
   db.add(new_content)
   db.commit()
   db.refresh(new_content)
   return new_content

# Get Latest Food Content
@router.get("/latest")
def get_latest_content(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    content = db.query(models.FoodContent).order_by(models.FoodContent.created_at.desc()).first()
    return content

# Get Food Content by Id
@router.get("/{id}")
def get_content_by_id(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    content = db.query(models.FoodContent).filter(models.FoodContent.id == id).first()
    if not content:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Content with id {id} doesn't exist")
    return content

# Delete Own Food Content
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_content(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    content = db.query(models.FoodContent).filter(models.FoodContent.id == id)
    if content.first() == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Content with id {id} doesn't exist")
    if content.first().owner_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail=f"You don't have access to delete the content with id {id}")
    content.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)

# Update Own Food Content
@router.put("/{id}", response_model = schemas.FoodContent)
def update_content(id: int, updated_content: schemas.ContentCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    content_query = db.query(models.FoodContent).filter(models.FoodContent.id == id)
    content = content_query.first()
    if content == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Content with id {id} doesn't exist")
    if content.owner_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail=f"You don't have access to edit the content with id {id}")
    content_query.update(updated_content.model_dump(), synchronize_session = False)
    db.commit()
    return  content_query.first()
# Import Libraries
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

# Activate Router
router = APIRouter(
    prefix = "/recipe",
    tags = ['Recipe']
)

# Get All Recipes
@router.get("/", response_model = List[schemas.RecipeBase])
def get_recipes(db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    recipes = db.query(models.Recipe).all()
    return recipes

# Create Recipe
@router.post("/", status_code = status.HTTP_201_CREATED, response_model = schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
   new_recipe = models.Recipe(owner_id = current_user.id,**recipe.model_dump())
   db.add(new_recipe)
   db.commit()
   db.refresh(new_recipe)
   return new_recipe

# Get Latest Recipe
@router.get("/latest")
def get_latest(db: Session = Depends(get_db)):
    recipe = db.query(models.Recipe).order_by(models.Recipe.created_at.desc()).first()
    return recipe

# Get Recipe by Id
@router.get("/{id}")
def get_recipe(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == id).first()
    if not recipe:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Recipe with id {id} doesn't exist")
    return recipe

# Get Recipe by Category
@router.get("/category/{category}")
def get_recipe_by_category(category: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    recipe = db.query(models.Recipe).filter(models.Recipe.category == category).all()
    if not recipe:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Category {category} doesn't exist")
    return recipe

# Delete Own Recipe
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_recipe(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == id)
    if recipe.first() == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Recipe with id {id} doesn't exist")
    if recipe.first().owner_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail=f"You don't have access to delete the recipe with id {id}")
    recipe.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)

# Update Own Recipe
@router.put("/{id}", response_model = schemas.Recipe)
def update_recipe(id: int, updated_recipe: schemas.RecipeCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    recipe_query = db.query(models.Recipe).filter(models.Recipe.id == id)
    recipe = recipe_query.first()
    if recipe == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Recipe with id {id} doesn't exist")
    if recipe.owner_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail=f"You don't have access to edit the recipe with id {id}")
    recipe.update(updated_recipe.model_dump(), synchronize_session = False)
    db.commit()
    return  recipe_query.first()
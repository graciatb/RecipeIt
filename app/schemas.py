from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class RecipeBase(BaseModel):
    title: str
    level: str
    category: str
    ingredients: str
    directions: str
    published: bool = True

class RecipeCreate(RecipeBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

class Recipe(RecipeBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config():
        from_attributes = True

class UserCreate(BaseModel): 
    email: EmailStr
    password: str

    class Config():
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class FoodContentBase(BaseModel):
    title: str
    desc: str
    topic: str
    published: bool = True

class ContentCreate(FoodContentBase):
    pass

class FoodContent(FoodContentBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut    

    class Config():
        from_attributes = True

class ReviewBase(BaseModel):
    id: int
    rating: int
    review: str
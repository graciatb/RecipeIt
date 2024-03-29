import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, CheckConstraint, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    level = Column(String, nullable=False)
    category = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)
    directions = Column(String, nullable = False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

    __table_args__ = (
        CheckConstraint(category.in_(['Beverage', 'Food']), name='category_name_check'),
    )

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class FoodContent(Base):
    __tablename__ = "foodContent"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    desc = Column(String, nullable = False)
    topic = Column(String, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class Review(Base):
    __tablename__ = "reviews"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    recipe_id = Column(Integer, ForeignKey("recipe.id", ondelete="CASCADE"), primary_key=True)
    rating = Column(Integer, nullable = False)
    review = Column(String, nullable = False)
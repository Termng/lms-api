from fastapi import APIRouter, HTTPException, Response, Depends, status
from .. import schema, models
from sqlalchemy.orm import Session
from ..database import engine, get_db


router = APIRouter(
    prefix= "/courses",
    tags=["Courses"]
)

@router.get("/")
def get_courses(db: Session= Depends(get_db)):
    all_courses= db.query(models.Course).all()
    return all_courses




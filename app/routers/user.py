from fastapi import APIRouter, HTTPException, Response, Depends, status
from .. import schema, models
from sqlalchemy.orm import Session
from ..database import engine, get_db


router = APIRouter(
    prefix= "/users",
    tags=["Users"]
)


@router.get("/")
def get_student(db: Session = Depends(get_db)):
    res_data = db.query(models.Students).all()
    return res_data


@router.get("/{id}")
def get_one_student(id: int, db: Session = Depends(get_db)):
    res_data_one = db.query(models.Students).filter(models.Students.id == id).first()
    
    if not res_data_one:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with the id {id} does not exist")
    return res_data_one


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.PostResponse)
def create_student(studProfile: schema.CreateStudent, db: Session = Depends(get_db)):
    createStudent = models.Students(**studProfile.model_dump())
    db.add(createStudent)
    db.commit()
    db.refresh(createStudent)
    return createStudent
    
    


@router.put("/{id}", response_model=schema.UpdateStudent)
def update_student(updateStud : schema.UpdateStudent, id: int, db: Session = Depends(get_db)):
    res_data = db.query(models.Students).filter(models.Students.id == id)
    updated_data = res_data.first()
    
    if updated_data == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} does not exist")
    res_data.update(updateStud.model_dump(), synchronize_session=False)
    
    db.commit()
    return updated_data



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_student(id: int, db: Session = Depends(get_db)):
    res_data = db.query(models.Students).filter(models.Students.id == id)
    to_delete = res_data.first()
    
    res_data.delete(synchronize_session=False)
    db.commit()
    
    if not to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post cannot be deeted as user with id = {id} does not exist")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    






from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import List



class CreateStudent(BaseModel):
    name: str
    email: EmailStr
    password: str
    # role: str

class GetStudent(BaseModel):
    name: str
    email: EmailStr
    # role: str

class UpdateStudent(BaseModel):
    name: str
    email: EmailStr
    
class PostResponse(BaseModel):
    id : int
    name: str
    email: EmailStr
    # role: str
    

class School(str, Enum):
    Engineering : "SOE"
    Product: "SOP"
    Business: "SOB"
    Data: "SOD"
    CreativeEconomy: "SOCE"

class CourseStatus(str, Enum):
    A: "Active"
    AR: "Archived"
    C: "Completed"
    CD: "Cancelled"
    
         
class Course(BaseModel):
    id: int
    course_name: str
    description: str
    instructor: str
    status: CourseStatus 
    course_duration: int
    school: School
    student: List[GetStudent]
    


    
    
    
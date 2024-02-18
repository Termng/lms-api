from pydantic import BaseModel, EmailStr, ConfigDict
from enum import Enum
from typing import List, Union

class GetStudent(BaseModel):
    name: str
    email: EmailStr
    # role: str    

class School(str, Enum):
    Engineering = "SOE"
    Product = "SOP"
    Business = "SOB"
    Data = "SOD"
    CreativeEconomy = "SOCE"

class CourseStatus(str, Enum):
    Active = "A"
    Archived = "AR"
    Completed = "C"
    Cancelled = "CD"

class Course(BaseModel):
    courseName: str
    description: str
    instructor: str
    course_duration: int
    status: Union[CourseStatus, str] 
    school: Union[School, str]

model_config = ConfigDict(arbitrary_types_allowed=True)

# student: List[GetStudent]

class CreateStudent(BaseModel):
    name: str
    email: EmailStr
    password: str
    course: Course
    

class UpdateStudent(BaseModel):
    name: str
    email: EmailStr
    
class PostResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

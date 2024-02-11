from pydantic import BaseModel, EmailStr


class createStudent(BaseModel):
    name: str
    email: EmailStr
    password: str
    # role: str

class getStudent(BaseModel):
    name: str
    email: EmailStr
    # role: str

class updateStudent(BaseModel):
    name: str
    email: EmailStr
    
class PostResponse(BaseModel):
    id : int
    name: str
    email: EmailStr
    # role: str


    
    
    
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base


class Students(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name =Column(String, nullable= False)
    email = Column(String, unique=True, nullable=False)
    password =Column(String, nullable= False)
    course_id = Column(String, ForeignKey("courses.id", ondelete='CASCADE'), nullable=False)
    course = relationship('Course')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, nullable= False)
    courseName=Column(String, nullable=False)
    description= Column(String, nullable=False)
    instructor= Column(String, nullable=False)
    status= Column(String, nullable=False)
    course_duration=Column(Integer, nullable=False)
    school= Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    student_id= Column(Integer, ForeignKey("student.id"), nullable=False)
    

    
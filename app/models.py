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
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
from sqlalchemy import Column, VARCHAR, INT

from db.models.base import BaseModel


class DBEmployee(BaseModel):

    __tablename__ = 'employees'

    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
    user_id = Column(INT())


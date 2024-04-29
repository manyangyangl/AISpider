from sqlalchemy import Column, String, Text, Integer, DateTime, func
from .metadata_base import Base


class Ecouncil(Base):
    __tablename__ = 'bayside'

    id = Column(Integer, primary_key=True, autoincrement=True)
    app_number = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=True, server_default=None)
    type_of_work = Column(Text, nullable=True, server_default=None)
    date_lodged = Column(Integer, nullable=True, server_default=None)
    cost = Column(String(255),nullable=True, server_default=None)
    determination_details = Column(String(255))
    determination_date = Column(Integer, nullable=True, server_default=None)
    application_stages_and_status = Column(Text, nullable=True, server_default=None)
    document = Column(Text, nullable=True, server_default=None)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


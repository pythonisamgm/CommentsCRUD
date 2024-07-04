from sqlalchemy import Column, Integer, String, TIMESTAMP, text, Date, func
from datetime import datetime
from core.comments_database import Base



class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    content = Column(String, nullable=False)
    #added_at = Column(Date, default=func.current_date(), nullable=False)

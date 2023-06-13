from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from ..db.sql import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP, TIME_TIMEZONE
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .users import User


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    votes = Column(Integer, default=0)
    owner_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    
    owner = relationship("User")
    
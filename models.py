from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class Post(Base):
    __tablename__ = "post"

    post_id = Column(Integer, primary_key= True, autoincrement = True)                  # No.
    writer = Column(Text, nullable= False)                                              # 작성자 
    content = Column(Text, nullable= False)                                             # 내용 
    title = Column(Text, nullable=False)                                                # 제목 
    time_created =  Column(DateTime(timezone=True), server_default = func.now() )       # 작성일 및 시간 



class Comment(Base):
    __tablename__ = "comment"

    comment_id = Column(Integer, primary_key = True, autoincrement= True)
    post_id = Column(Integer, ForeignKey("post.post_id"))
    writer = Column(Text, nullable = False)
    content = Column(Text, nullable=False)
    post = relationship("Post", backref = "comment")

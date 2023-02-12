from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy import Column
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)




# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String(100))
#     last_name = Column(String(100))
#     email = Column(String(100), unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
    
#     posts = relationship('Post', back_populates='owner')


# class Post(Base):
#     __tablename__ = 'posts'
    
#     title = Column(String(100))
#     description = Column(String(5000))
#     time_created = Column(DateTime(timezone=True), server_default=func.now())

#     owner_id = Column(Integer, ForeignKey("users.id"))
#     owner = relationship('User', back_populates='posts')

# metadata = MetaData()
# user_table = Table('users', metadata,
#     Column('id', Integer, primary_key=True),
#     Column('first_name', String(100)),
#     Column('last_name', String(100)),
#     Column('email', String(100), unique=True, index=True),
#     Column()

# )
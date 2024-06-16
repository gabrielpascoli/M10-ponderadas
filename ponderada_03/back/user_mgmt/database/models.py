from sqlalchemy import Column, Integer, String
from database.database import db

class User(db.Model):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False)
  password = Column(String(50), nullable=False)

  def __repr__(self):
    return f'''
    User:[
      id:{self.id},
      username:{self.username},
      email:{self.email},
      password:{self.password}
    ]
    '''
  
  def serialize(self):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email,
      "password": self.password
    }
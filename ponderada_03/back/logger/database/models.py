from sqlalchemy import Column, Integer, String
from database.database import db

class Log(db.Model):
  __tablename__ = 'logs'

  id       = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String(50), nullable=False)
  email    = Column(String(50), nullable=False)
  action   = Column(String(50), nullable=False)
  datetime = Column(String(50), nullable=False)

  def __repr__(self):
    return f'''
    User:[
    id:{self.id},
    username:{self.username},
    email:{self.email},
    action:{self.action},
    datetime:{self.datetime}
    ]
    '''
  
  def serialize(self):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email,
      "action": self.action,
      "datetime": self.datetime
    }
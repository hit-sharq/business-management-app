from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine for the SQLite database
engine = create_engine('postgresql://postgres:joshualee087@localhost:5432/inventory_management_app')


Session = sessionmaker(bind=engine)
Session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    email = Column(String(255), unique=True)
    
# Base.metadata.create_all(engine)
    def create_user(self, user):
        Session.add(user)
        Session.commit()    
    
    def get_user_by_username(self, username):
        return Session.query(User).filter_by(username=username).first()
    
user_1 = User(username= "denis", email="denis@example.com", password="password")
# print(user_1.get_user_by_username("joshua").password)

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine for the SQLite database
engine = create_engine('postgresql://postgres:joshualee087@localhost:5432/inventory_management_app')

Session = sessionmaker(bind=engine)
Session = Session()
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    price = Column(Float)
    quantity = Column(Integer)
    description = Column(String(255))
    category = Column(String(255))
    user_id = Column(Integer)

Base.metadata.create_all(engine)

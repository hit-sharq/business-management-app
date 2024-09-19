from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from prettytable import PrettyTable

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
    category = Column(String)
    user_id = Column(Integer)

    def update_product(self):
        pass

#Base.metadata.create_all(engine)
def add_product(product):
    Session.add(product)
    Session.commit()
def view_product():
    table = PrettyTable()
    table.field_names = ['id', 'name', 'price', 'description', 'category']
    all_products = Session.query(Product).order_by(Product.id.asc()).all()
    count = 0
    for product in all_products:
        count += 1
        table.add_row([count, product.name, product.price, product.description, product.category])
    print(table)
def search_products(name):
    products = Session.query(Product).filter(Product.name.contains(name)).all()
    table = PrettyTable()
    table.field_names = ['No', 'name', 'price', 'description', 'category']
    for product in products:
        table.add_row([product.id, product.name, product.price, product.description, product.category])
    print(table)
prod1  = Product(name="itel", description="good", category="good", user_id  = 1)
# view_product()

def update_product():
    product_name = input('Enter name of the product you want to update: ')
    products = Session.query(Product).filter(Product.name.contains(product_name)).all()
    table = PrettyTable()
    table.field_names = ['id', 'name', 'price', 'description', 'category']
    for product in products:
        table.add_row([product.id, product.name, product.price, product.description, product.category])
    print(table)
    print('Choose the id of the product you want to update from above')
    product_id = input("Enter product id to update: ")
    field = input('Enter field to update (name, price, description, category): ')
    new_value = input('Enter new value: ')
    product = Session.query(Product).get(product_id)
    setattr(product, field, new_value)
    Session.commit()
    print("Product updated successfully!")

def delete_product():
    product_name = input('Enter name of the product you want to delete: ')
    products = Session.query(Product).filter(Product.name.contains(product_name)).all()
    table = PrettyTable()
    table.field_names = ['id', 'name', 'price', 'description', 'category']
    for product in products:
        table.add_row([product.id, product.name, product.price, product.description, product.category])
    print(table)
    print('Choose the id of the product you want to delete from above')
    product_id = input("Enter product id to delete: ")
    product = Session.query(Product).get(product_id)
    Session.delete(product)
    Session.commit()
    print("Product deleted successfully!")

def view_by_category(category):
    products = Session.query(Product).filter(Product.category.contains(category)).all()
    table = PrettyTable()
    table.field_names = ['id', 'name', 'price', 'description', 'category']
    for product in products:
        table.add_row([product.id, product.name, product.price, product.description, product.category])
    print(table)
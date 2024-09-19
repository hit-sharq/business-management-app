from user import User
import getpass
from products import Product, add_product, view_product,search_products,update_product,delete_product,view_by_category
from sqlalchemy.orm import  Session
#create a propmt for user login
def signup():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    email = input("Enter an email: ")

    new_user = User(username=username, password=password, email=email)
    new_user.create_user(new_user)
    print("User created successfully!")
    
# signup()
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    user = User()
    user = user.get_user_by_username(username)

    if user and user.password == password:
        print("Login successful!")
    else:
        print("Invalid credentials!")
        login()
def add_product_to_inventory():
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        description = input("Enter product description: ")
        category = input("Enter product category: ")
        user_id = 1  # assuming that the user_id is stored in a database and retrieved from the session

        new_product = Product(name=name, price=price, quantity=quantity, description=description, category=category, user_id=user_id)
        add_product(new_product)
        print("Product added successfully!")
        choices()

def choices():
        print(''' 
        enter number provided for any choice \n 
          1. Add a product \n 
          2. View  all products \n  
          3. Search for products \n
          4.view by category \n 
          5. update \n 
          6. delete \n 
          
        
    ''')
        choice1 = input('Enter choice no')
        if choice1 == '1':
            add_product_to_inventory()
        elif choice1 == '2':
            view_product()
        elif choice1 == '3':
            name = input("Enter product name to search: ")
            search_products(name)
        elif choice1 == '4':
            category = input("Enter category to view: ")
            view_by_category(category)  
        elif choice1 == '5':
            update_product()
        elif choice1 == '6':
            delete_product()
        choices()

        

print("Do you want to login or signup?")
choice = input("Enter 'login' or 'signup': ")

if choice.lower() == "login":
    login()
    choices()
elif choice.lower() == "signup":
    signup()
    choices()
else:
    print("Invalid choice!")



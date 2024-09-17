from user import User
import getpass
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

print("Do you want to login or signup?")
choice = input("Enter 'login' or 'signup': ")

if choice.lower() == "login":
    login()
elif choice.lower() == "signup":
    signup()
else:
    print("Invalid choice!")

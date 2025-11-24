# CT-13 User Signup Functionality

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password   # (No encryption for demo)
        self.email = email

    def __str__(self):
        return f"User Created: {self.username} ({self.email})"


# Test Case
def signup():
    print("📦 Parcel System — User Signup")
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")

    user = User(username, password, email)
    print("\nSignup successful!")
    print(user)


if __name__ == "__main__":
    signup()

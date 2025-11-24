# CT-16 | User Management System Simulation

class UserManagement:
    def __init__(self):
        self.users = {}  # store users as {username: role}

    def add_user(self, username, role):
        if username in self.users:
            print(f"User '{username}' already exists!")
        else:
            self.users[username] = role
            print(f"User '{username}' added as {role}.")

    def update_role(self, username, new_role):
        if username in self.users:
            self.users[username] = new_role
            print(f"Updated '{username}' role to {new_role}.")
        else:
            print(f"User '{username}' not found.")

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            print(f"User '{username}' removed from system.")
        else:
            print(f"User '{username}' does not exist.")

    def list_users(self):
        if not self.users:
            print("No users in the system.")
        else:
            print("\n📌 Current Users:")
            for u, r in self.users.items():
                print(f" - {u} → {r}")


# -------- Test Case --------
if __name__ == "__main__":
    admin = UserManagement()

    admin.add_user("priya", "Admin")
    admin.add_user("harsha", "Customer")
    admin.add_user("ravi", "Delivery Agent")

    admin.list_users()

    admin.update_role("harsha", "Agent")
    
    admin.delete_user("ravi")

    admin.list_users()

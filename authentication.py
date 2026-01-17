from data import load_data, save_data

class Auth:
    def signup(self, username, password):
        data = load_data()

        if any(user["username"] == username for user in data["users"]):
            print("Username already exists")
            return

        data["users"].append({
            "username": username,
            "password": password
        })

        save_data(data)
        print("Account created successfully")

    def login(self, username, password):
        data = load_data()

        if any(
            user["username"] == username and user["password"] == password
            for user in data["users"]
        ):
            print(f"Welcome {username}")
            return True

        print("Invalid credentials")
        return False

from authentication import Auth
from chat import Chat

auth = Auth()
chat = Chat()

print("=== Mini Chat System ===")

while True:
    choice = input("\n1. Signup\n2. Login\n3. Exit\nChoose: ")

    if choice == "1":
        u = input("Username: ")
        p = input("Password: ")
        auth.signup(u, p)

    elif choice == "2":
        u = input("Username: ")
        p = input("Password: ")

        if auth.login(u, p):
            while True:
                print("\n1. Send Message\n2. View Inbox\n3. Logout")
                c = input("Choose: ")

                if c == "1":
                    to = input("Send to: ")
                    msg = input("Message: ")
                    chat.send_message(u, to, msg)

                elif c == "2":
                    chat.inbox(u)

                elif c == "3":
                    break

    elif choice == "3":
        print("Goodbye!")
        break

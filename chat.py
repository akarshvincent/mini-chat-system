from data import load_data, save_data

class Chat:
    def send_message(self, sender, receiver, text):
        data = load_data()

        if not any(user["username"] == receiver for user in data["users"]):
            print(" Receiver does not exist")
            return

        data["messages"].append({
            "from": sender,
            "to": receiver,
            "text": text
        })

        save_data(data)
        print("📨 Message sent")

    def inbox(self, username):
        data = load_data()
        messages = [m for m in data["messages"] if m["to"] == username]

        if not messages:
            print("No messages")
            return

        print("\n Inbox:")
        for msg in messages:
            print(f"From {msg['from']}: {msg['text']}")

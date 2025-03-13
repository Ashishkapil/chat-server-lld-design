from client_manager import ClientManager


class ChatServer:
    def __init__(self):
        self.client_manager = ClientManager()

    def send_message(self, user_id, receiver_id, message):
        self.client_manager.send_message(user_id, receiver_id, message)

    def get_messages(self, user_id, sender_id):
        return self.client_manager.get_messages(user_id, sender_id)

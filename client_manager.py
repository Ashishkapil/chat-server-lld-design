# from chat_room import ChatRoom
from User import User


class ClientManager:
    def __init__(self):
        self.user = User()

    def send_message(self, user_id, receiver_id, message):
        self.user.send_message(user_id, receiver_id, message)

    def get_messages(self, user_id, sender_id):
        return self.user.get_messages(user_id, sender_id)

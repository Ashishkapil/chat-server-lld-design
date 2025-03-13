from Message import Message

class User:
    def __init__(self):
        self.message_list = []

    def send_message(self, user_id, receiver_id, message):
        message = Message(user_id, receiver_id, message)
        self.message_list.append(message)
        print("Message list : ", self.message_list)


    def get_messages(self, user_id, sender_id):
        messages = []
        for message in self.message_list:
            if message.sender_id == sender_id and message.receiver_id == user_id:
                messages.append(message)

        messages = [msg for msg in self.message_list if msg.sender_id == sender_id and msg.receiver_id == user_id]

        self.message_list = [msg for msg in self.message_list if msg not in messages]

        for message in self.message_list:
            if message.sender_id == sender_id and message.receiver_id == user_id:
                self.message_list.remove(message)

        return messages

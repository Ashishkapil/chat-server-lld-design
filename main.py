"""
chat server


Requirements:
one-to-one chat
Text messages
No persistence
HTTP polling - check timeout

Good to have :-
Acknowledge
Encryption
Auth


User mapping

"""


from fastapi import FastAPI
from chat_server import ChatServer

app = FastAPI()
chat_server = ChatServer()


@app.post("/chat/{user_id}")
def send_message(user_id: str, receiver_id: str, message: str):
    try:
        chat_server.send_message(user_id, receiver_id, message)
        return 200
    except Exception as e:
        print(f"Exception occurred while sending message - user: {user_id}")
        return 500


@app.get("/chat/{user_id}")
def poll_message(user_id: str, sender_id: str):
    messages = chat_server.get_messages(user_id, sender_id)
    return messages











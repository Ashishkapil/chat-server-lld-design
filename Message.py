from dataclasses import dataclass

@dataclass
class Message:
    sender_id: str
    receiver_id: str
    text: str
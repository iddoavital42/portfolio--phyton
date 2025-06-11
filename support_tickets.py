import uuid
from datetime import datetime


class Ticket:
    def __init__(self, name, email, subject, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.subject = subject
        self.description = description
        self.created_at = datetime.now()
        self.resolved = False

    def close(self):
        self.resolved = True
    def to_dict(self):
        return {
          "id": self.id,
            "name": self.name,
            "email": self.email,
            "subject": self.subject,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at    
        }
    
    def __str__(self):
        return f"[{self.status}] {self.subject} ({self.id})\nBy: {self.name} <{self.email}>\n{self.description}\nCreated: {self.created_at}"
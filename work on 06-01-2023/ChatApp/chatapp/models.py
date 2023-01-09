from . import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(20), nullable=False)
    receiver = db.Column(db.String(20), nullable=False)
    msg = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.sender} {self.receiver}'

    def __init__(self, sender, reciver, msg):
        self.sender = sender
        self.receiver = reciver
        self.msg = msg

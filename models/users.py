from config import db 

class User(db.Model):
    __tablename__ = 'users'
    username=db.Column(db.String(30), primary_key=True)
    password=db.Column(db.String(30),nullable=False)
    usertype=db.Column(db.String(10),nullable=False)

    def __init__(self,username,password,usertype):
        self.username=username
        self.password=password
        self.usertype=usertype

    def serialize(self):
        return {
            'username': self.username,
            'usertype': self.usertype
        }

    def __repr__(self):
        return str(self.serialize())
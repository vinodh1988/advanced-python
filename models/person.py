from config import db 

class Person(db.Model):
    __tablename__ = 'people'
    sno=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    city=db.Column(db.String(30),nullable=False)

    def __init__(self,sno,name,city):
        self.sno=sno
        self.name=name
        self.city=city

    def serialize(self):
        return {
            'sno': self.sno,
            'name': self.name,
            'city': self.city
        }

    def __repr__(self):
        return str(self.serialize())
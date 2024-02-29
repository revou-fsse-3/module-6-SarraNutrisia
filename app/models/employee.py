from app.utils.database import db

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    phone_number = db.Column(db.Integer, nullable=True)
    role = db.Column(db.String(100), nullable=True)
    schedule = db.Column(db.String(100), nullable=True)

    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "role": self.role,
            "schedule": self.schedule
        }
from app.utils.database import db

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(100), nullable=True)
    special_requirements = db.Column(db.String(100), nullable=True)

    
    def as_dict(self):
        return {
            "id": self.id,
            "species": self.species,
            "age": self.age,
            "gender": self.gender,
            "special_requirements": self.special_requirements
        }
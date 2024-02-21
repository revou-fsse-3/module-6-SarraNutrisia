from flask import Blueprint, request
from app.models.animal import Animal
from app.utils.database import db

animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route("/", methods=["GET"])
def get_animals():
    try:
        
        animals = Animal.query.all()

        return [animal.as_dict() for animal in animals], 200
    except Exception as e:
        return e, 500
    

@animal_blueprint.route("/<int:animal_id>", methods=["GET"])
def get_animal_by_id(animal_id):
    try:
       
        animal = Animal.query.get(animal_id)

        return animal.as_dict(), 200
    except Exception as e:
        return e, 500


@animal_blueprint.route("/", methods=["POST"])
def create_animal():
    try :
       
        data = request.json
       
        animals = Animal()
       
        animals.species = data['species']
        animals.age = data['age']
        animals.gender = data['gender']
        animals.special_requirements = data['special_requirements']
        
        db.session.add(animals)
        db.session.commit()
        return 'Successfully Created', 200
    except Exception as e:
        return e, 500


@animal_blueprint.route("/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    try:
      
        animal = Animal.query.get(animal_id)
       
        data = request.json
        
        animal.species = data['species']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.special_requirements = data['special_requirements']
        
        db.session.commit()
        return 'Successfully Updated', 200
    except Exception as e:
        return e, 500


@animal_blueprint.route("/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    try:
        
        animal = Animal.query.get(animal_id)
        
        db.session.delete(animal)
        db.session.commit()
        return 'Successfully Deleted', 200
    except Exception as e:
        return e, 500
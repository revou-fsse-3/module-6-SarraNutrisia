from flask import Blueprint, request
from app.models.employee import Employees
from app.utils.database import db

employee_blueprint = Blueprint('employee_endpoint', __name__)


@employee_blueprint.route("/", methods=["GET"])
def get_employees():
    try:
        
        employees = Employees.query.all()
        return [employee.as_dict() for employee in employees], 200
    except Exception as e:
        return e, 500


@employee_blueprint.route("/<int:employee_id>", methods=["GET"])
def get_employee_by_id(employee_id):
    try:
       
        employee = Employees.query.get(employee_id)
        return employee.as_dict(), 200
    except Exception as e:
        return e, 500


@employee_blueprint.route("/", methods=["POST"])
def create_employee():
    try:
        
        data = request.json
        
        employee = Employees()
        
        employee.name = data['name']
        employee.email = data['email']
        employee.phone_number = data['phone_number']
        employee.role = data['role']
        employee.schedule = data['schedule']
        
        db.session.add(employee)
        db.session.commit()
        return 'Successfully Created', 200
    except Exception as e:
        return e, 500


@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    try:
       
        employee = Employees.query.get(employee_id)
       
        data = request.json
        
        employee.name = data['name']
        employee.email = data['email']
        employee.phone_number = data['phone_number']
        employee.role = data['role']
        employee.schedule = data['schedule']
        
        db.session.commit()
        return 'Successfully Updated', 200
    except Exception as e:
        return e, 500


@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    try:
        
        employee = Employees.query.get(employee_id)
       
        db.session.delete(employee)
        db.session.commit()
        return 'Successfully Deleted', 200
    except Exception as e:
        return e, 500
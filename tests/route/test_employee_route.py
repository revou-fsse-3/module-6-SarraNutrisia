def test_get_employees_status_code(test_app):
    response = test_app.get("/employee/")
    assert response.status_code == 200

def test_put_employees_update(test_app):
    data = {
        "name": "Richard",
        "email": "richard@gmail.com",
        "phone_number": 81698421369,
        "role": "Janitor",
        "schedule": "All Day"
    }
    response = test_app.put("/employee/8", json=data)
    print(response.json)
    assert response.status_code == 200
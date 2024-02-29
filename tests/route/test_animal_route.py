def test_get_animals_status_code(test_app):
    response = test_app.get("/animal/")
    assert response.status_code == 200

def test_put_animals_update(test_app):
    data = {
        "species": "Crocodile",
        "age": 7,
        "gender": "Male",
        "special_requirements": "Small Mammal"
    }
    response = test_app.put("/animal/7", json=data)
    print(response.json)
    assert response.status_code == 200






    
     

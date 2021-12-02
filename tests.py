from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_employees():
    data = {'email': 'magna.Cras.convallis@ipsumleo.edu'}
    response = client.get("/employees", json=data)
    assert response.json() == {'employees': [{
        "name": "Ivor Casey",
        "email": "magna.Cras.convallis@ipsumleo.edu",
        "age": 63,
        "company": "Amazon",
        "join_date": "2007-11-19T11:45:01-08:00",
        "job_title": "director",
        "gender": "male",
        "salary": 2572
    }]}
    assert response.status_code == 200

import requests
import json
from random import randint

def test_get_read_users_me():
    response = requests.get("http://localhost:8000/users/me")
    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}

def test_get_read_users():
    response = requests.get("http://localhost:8000/users/")
    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}

def test_get_read_user():
    number = 3
    response = requests.get("http://localhost:8000/users/" + (str(number)))
    assert response.status_code == 200
    assert (response.json().get('id')) == number


def test_get_read_user_heaviest_lift():
    response = requests.get("http://localhost:8000/users/3/heaviestlift")
    assert response.status_code == 200
    assert (response.json().get('amount')) > 0

def test_get_read_user_lifts():
    response = requests.get("http://localhost:8000/users/3/lifts")
    assert response.status_code == 200
    assert response.json() != None

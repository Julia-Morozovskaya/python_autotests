import requests
import pytest

def test_trainers():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200



def test_hadz():
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1194'})
    assert response.json() ['trainer_name'] == 'Hadzeka'
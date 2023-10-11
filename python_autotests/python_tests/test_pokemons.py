import requests
import pytest

token = "YOUR TOKEN"
host = 'https://api.pokemonbattle.me:9104'
trainer_id = 2574 #YOUR TRAINER_ID

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': trainer_id})
    assert response.status_code == 200
    assert response.json()["trainer_name"] == "pythonyash"

def test_body_info ():
    response = requests.get(f'{host}/trainers', params={'trainer_id': trainer_id})
    assert response.status_code == 200

def test_create_pokemon ():
    response = requests.post(f'{host}/pokemons', headers={"Content-Type": "application/json", "trainer_token": token},
                             json={"name": "generate", "photo": "generate"})
    assert response.json()["message"] == "Покемон создан"


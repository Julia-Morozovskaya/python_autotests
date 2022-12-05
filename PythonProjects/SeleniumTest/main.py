import requests
token = 'e3f173ecf40042d06e4cc865f9a2f486'

'''response_post = requests.post( 'https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token, 'Accept' : 'application/json'}, json= {
    "name": "Haunter",
    "photo": "https://www.pngplay.com/wp-content/uploads/11/Haunter-Pokemon-PNG-Photos.png"
})
print(response_post.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'Accept' : 'application/json', 'trainer_token': token}, json={
     "pokemon_id": 1345,
     "name": "Хаунтер",
     "photo": "https://www.pngplay.com/wp-content/uploads/11/Haunter-Pokemon-PNG-Photos.png"
})
print(response_put.text)'''

response_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'Accept' : 'application/json', 'trainer_token': token}, json={
   "pokemon_id": 1345
})
print(response_post.text)
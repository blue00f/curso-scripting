import requests

API_ESPECIES_POKEMON = "https://pokeapi.co/api/v2/pokemon/"

def getInfoPokemon(nombrePokemon):
  buscarPokemon = f'{API_ESPECIES_POKEMON}/{nombrePokemon.lower()}/'
  res = requests.get(buscarPokemon)
  if res.status_code == 200:
    datosPokemon = res.json()

    infoPokemon = {
      'idPokemon': datosPokemon['id'],
      'nombre': datosPokemon['name'],
      'tipos': [tipo['type']['name'] for tipo in datosPokemon['types']],
      'habilidades': [habilidad['ability']['name'] for habilidad in datosPokemon['abilities']]
    }
    return infoPokemon
  else:
    return res.status_code

nombrePokemon = input("Ingresa el nombre de un Pokemon: ")
infoPokemon = getInfoPokemon(nombrePokemon)

if infoPokemon == 404:
  print('El pokemon ingresado no existe')
else:
  print(f'Nombre: {infoPokemon['nombre'].capitalize()}')
  print(f'ID: {infoPokemon['idPokemon']}')
  print('Tipos:')
  for tipo in infoPokemon['tipos']:
    print(f'- {tipo}')
  print('Habilidades:')
  for habilidad in infoPokemon['habilidades']:
    print(f'- {habilidad}')
    
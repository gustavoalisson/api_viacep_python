import requests

name_filme = input('Digite o nome do filme: ')

requisicao = requests.get(f'http://www.omdbapi.com/?t={name_filme}&apikey=7d1c5a0d')

print(requisicao.text)
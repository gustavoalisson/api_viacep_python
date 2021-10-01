import requests
import json


def requisicao(name_filme):
    key = '7d1c5a0d'
    try:
        req = requests.get(f'http://www.omdbapi.com/?t={name_filme}&apikey={key}').text
        filme = json.loads(req)
        return filme
    except Exception as e:
        print('Fail requests ', e)
        exit()
        
def detalhes_filme(filme):
    
    print('======> FILME ENCONTRADO <====== ')

    print('Informações do filme: ')
    print()    
    print(f"Nome do filme: {filme['Title']}")
    print(f"Ano: {filme['Year']}")
    print(f"Data de Lançamento: {filme['Released']}")
    print(f"Gênero: {filme['Genre']}")


def main():
    sair = False
    
    print('======> CONSULTA DE FILME <====== ')

    while not sair:
        pesquisar_filme = input('Digite o nome do filme: ')
        
        filme = requisicao(pesquisar_filme)
        if 'Error' not in filme:
            detalhes_filme(filme)
        else:
            print('Filme não encontrado!') 
        
        op = input('Escolha uma opção: 1 - Continuar pesquisando filme / 2 - SAIR \n')
        
        if op == '1':
            main()
        elif op == '2':
            # sair = True
            print('Saindo...')
            exit()            

if __name__ == '__main__':
    main()
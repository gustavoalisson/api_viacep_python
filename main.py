import requests
import json

# * Consulta CEP
def main():  
    print('------------------ CONSULTAR CEP ------------------')

    my_cep = input('Digite um CEP: ')
    
    if len(my_cep) != 8:
        print('Quantidade de digitos inválido!')
        exit()

    request = requests.get(f'https://viacep.com.br/ws/{my_cep}/json/unicode').text

    converte_lista = json.loads(request)

    if 'erro' not in converte_lista:
        print('==>CEP ENCONTRADO<==')
        print(f" CEP: {converte_lista['cep']} \n Logradouro: {converte_lista['logradouro']} \n Cidade: {converte_lista['localidade']} \n Bairro: {converte_lista['bairro']} \n Estado: {converte_lista['uf']}")
    else:
        print('CEP INVÁLIDO')
    print('---------------------------------------')
    option = input('Deseja encontrar um novo CEP? [S] para sim / [N] para não: \n')
    
    if option == 'S'.lower():
        main()
    elif option == 'N'.lower():
        print('Saindo...')
    else:
        print('Opção inválida. Encerrando!')
        exit()        

if __name__ == '__main__':
    main()           

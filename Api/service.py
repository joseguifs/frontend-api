import requests


class Auth:
    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8080/api/v1/'
    
    def __get_token_url(self):
        return f'{self.__base_url}authentication/token/'

    def get_token(self, username, password):
        url = self.__get_token_url()
        payload = {
            "username":username,
            "password":password
        }

        try:
            response = requests.post(url = url, json = payload)
            response.raise_for_status()
            data_token = response.json()
            return data_token['access']
        except requests.exceptions.HTTPError:
            raise ValueError(f'Credenciais inválida') 
    
    def __get_genres_url(self):
        return f'{self.__base_url}genres/'

    def get_genres(self, headers):
        url = self.__get_genres_url() 

        try:
            response = requests.get(url = url, headers = headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            raise ValueError("A autenticação falhou faça login novamente")
        
    def get_genre_detail(self, pk, headers):
        url = f'{self.__get_genres_url()}{pk}/'
        try:
            response = requests.get(url = url, headers = headers)
            response.raise_for_status() # ← Isso lança uma exceção se o status for 4xx ou 5xx
            return response.json()
        except requests.exceptions.HTTPError:
            raise ValueError()
        
    def post_genre(self, payload, headers):
        url = self.__get_genres_url()
        try:
            response = requests.post(url = url, json = payload, headers = headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise ValueError(f'{response.json()['name'][0]}') # response.json() == {'name':['messagem']}
        
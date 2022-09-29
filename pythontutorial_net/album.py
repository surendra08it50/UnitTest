import requests


def find_album_by_id(id):
    url = f'https://jsonplaceholder.typicode.com/albums/{id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['title']
    else:
        return None
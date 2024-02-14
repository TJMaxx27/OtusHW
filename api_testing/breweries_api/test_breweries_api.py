import requests
import pytest
import json
import os

base_url = 'https://api.openbrewerydb.org'

def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)

def brewery_id():
    file_path = get_path('breweries.json')
    with open(file_path, 'r') as file:
        breweries_data = json.load(file)
    return [brewery['id'] for brewery in breweries_data]


def brewery_names():
    file_path = get_path('breweries.json')
    with open(file_path, 'r') as file:
        breweries_data = json.load(file)
    return [brewery['name'] for brewery in breweries_data]


def test_get_breweries():
    response = requests.get(f'{base_url}/breweries')
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize('brewery_id', brewery_id())
def test_get_brewery_id(brewery_id):
    response = requests.get(f'{base_url}/breweries/{brewery_id}')
    assert response.status_code == 200
    assert response.json()['id'] == brewery_id


@pytest.mark.parametrize('brewery_name', brewery_names())
def test_search_breweries_by_name(brewery_name):
    response = requests.get(f'https://api.openbrewerydb.org/breweries', params={'name': brewery_name})
    assert response.status_code == 200
    found = any(brewery['name'].lower() == brewery_name.lower() for brewery in response.json())
    assert found, f"Не удалось найти пивоварню: {brewery_name}"


@pytest.mark.parametrize('brewery_website_url', ['http://www.405brewing.com','http://www.512brewing.com', 'https://www.1ofusbrewing.com'])
def test_get_brewery_website_url(brewery_website_url):
    response = requests.get(f'{base_url}/breweries')
    assert response.status_code == 200
    assert any(brewery.get('website_url') == brewery_website_url for brewery in response.json())


@pytest.mark.parametrize('state', ['California', 'Texas', 'New York', 'Florida', 'Oregon'])
def test_search_breweries_by_state(state):
    response = requests.get(f'{base_url}/breweries', params={'by_state': state})
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery['state'] == state


if __name__ == "__main__":
    breweries_data = get_path('breweries.json')
    pytest.main()




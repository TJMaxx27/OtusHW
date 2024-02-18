import requests
import json
import pytest


base_url = 'https://dog.ceo/api'

response_all_breeds = requests.get(f'{base_url}/breeds/list/all')
data_all_breeds = json.loads(response_all_breeds.text)

dog_breed_list = [breed for breed in data_all_breeds['message'].keys()]
all_breeds_with_subbreeds = [
    (breed, subbreeds) for breed, subbreeds in data_all_breeds['message'].items() if subbreeds
]


def test_get_base_url():
    response = requests.get(base_url)
    assert response.status_code == 200


@pytest.mark.parametrize("breed", dog_breed_list)
def test_get_breeds_list_all(breed):
    response = requests.get(f'{base_url}/breeds/list/all')
    data = json.loads(response.text)
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert 'message' in data
    assert breed in data['message']


@pytest.mark.parametrize("breed, subbreeds", all_breeds_with_subbreeds)
def test_get_subbreeds_list(breed, subbreeds):
    response = requests.get(f'{base_url}/breed/{breed}/list')
    data = json.loads(response.text)
    assert response.status_code == 200
    assert data['status'] == 'success'
    if 'message' in data and isinstance(data['message'], list):
        for subbreed in subbreeds:
            assert subbreed in data['message']
    elif not subbreeds:
            assert not data['message']


def test_get_random_image():
    response = requests.get(f'{base_url}/breeds/image/random')
    data = json.loads(response.text)
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert 'message' in data


@pytest.mark.parametrize("breed", dog_breed_list)
def test_get_random_images_by_breed(breed):
    response = requests.get(f'{base_url}/breed/{breed}/images/random/3')
    data = json.loads(response.text)
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert 'message' in data
    try:
        assert len(data['message']) == 3
    except AssertionError:
        print(f"Предупреждение: у породы {breed} менее 3 фотографий. Фактический результат: {len(data['message'])}")

if __name__ == "__main__":
    pytest.main()
import requests
import pytest


base_url = 'https://jsonplaceholder.typicode.com'


def test_get_base_url():
    response = requests.get(f'{base_url}/users')
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize('user_id', [1,2,3])
def test_get_users_id(user_id):
    response = requests.get(f'{base_url}/users/{user_id}')
    assert response.status_code == 200
    assert response.json()['id'] == user_id


@pytest.mark.parametrize('user_id', [1,2,3])
def test_get_post_by_user(user_id):
    response = requests.get(f'{base_url}/posts', params={'userId': user_id})
    assert response.status_code == 200
    for post in response.json():
        assert post['userId'] == user_id


@pytest.mark.parametrize('post_id',[1,2,3])
def test_get_comments_by_post(post_id):
    response = requests.get(f'{base_url}/comments', params={'postId': post_id})
    assert response.status_code == 200
    for comment in response.json():
        assert comment['postId'] == post_id


def test_create_post():
    data = {
        'userId': 1,
        'title': 'Test post',
        'body': 'Test massage'
    }
    response = requests.post(f'{base_url}/posts', json=data)
    assert response.status_code == 201
    assert 'id' in response.json()


def test_delete_post():
    data = {
        'userId': 1,
        'title': 'Test post',
        'body': 'Test massage'
    }
    response = requests.post(f'{base_url}/posts', json=data)
    assert response.status_code == 201
    post_id = response.json()['id']
    response = requests.delete(f'{base_url}/posts/{post_id}')
    assert response.status_code == 200
    response = requests.get(f'{base_url}/posts/{post_id}')
    assert response.status_code == 404


if __name__ == "__main__":
    pytest.main()
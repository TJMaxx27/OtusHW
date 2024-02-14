import pytest
import requests

@pytest.mark.parametrize("url, status_code", [
    ("https://mail.ru", 200),
    ("https://ya.ru", 200),
    ("https://ya.ru/sfhfh", 404),
])
def test_check_url_status(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code, f"Статус ответа не соответствует ожидаемому. Получено: {response.status_code}, ожидалось: {status_code}"




import requests
from conftest import HEADERS, BASE_URL
import uuid


def test_get_existing_project_by_id(created_project):
    """
    Позитивный тест: получение данных только что созданного валидного проекта.
    Проверяет структуру ответа и совпадение ключевых полей.
    """
    project_id, original_data = created_project

    response = requests.get(
        f"{BASE_URL}/projects/{project_id}", headers=HEADERS
    )

    assert (
        response.status_code == 200
    ), f"Ожидался статус 200, получен {response.status_code}. Текст: {response.text}"

    data = response.json()

    assert data["id"] == project_id
    assert data["title"] == original_data["title"]
    assert isinstance(data.get("boards"), list)


def test_get_nonexistent_project_returns_404():
    """
    Негативный тест: попытка получить проект по заведомо несуществующему UUID.
    Стабилен, так как использует фейковый ID, которого нет в базе.
    """
    fake_uuid = str(uuid.uuid4())

    response = requests.get(
        f"{BASE_URL}/projects/{fake_uuid}", headers=HEADERS
    )

    assert response.status_code in [404, 403], (
        f"Для несуществующего ресурса ожидается 404 или 403, получено {response.status_code}. "
        f"Текст: {response.text}"
    )


def test_get_project_without_api_key():
    """
    Негативный тест: отсутствие заголовка авторизации.
    Крайне стабилен, так как проверяет системную логику безопасности.
    """
    any_uuid = str(uuid.uuid4())

    response = requests.get(f"{BASE_URL}/projects/{any_uuid}")

    assert response.status_code in [
        401,
        403,
    ], f"Запрос без ключа должен быть отклонен с кодом 401 или 403, получено {response.status_code}"

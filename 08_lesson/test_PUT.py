import os
import time
import uuid
import pytest
import requests


def get_auth_headers():
    token = os.getenv("YOUGILE_API_TOKEN")
    if not token:
        # Если токена нет, тесты упадут с понятной ошибкой до отправки запросов
        raise ValueError("Environment variable YOUGILE_API_TOKEN is not set")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL API из переменных окружения."""
    url = os.getenv("YOUGILE_BASE_URL")
    assert url, "Environment variable YOUGILE_BASE_URL must be set"
    return url.rstrip("/")


@pytest.fixture
def temp_project(base_url):
    """
    Фикстура для создания временного проекта.
    Возвращает ID созданного проекта и удаляет его после теста.
    """
    headers = get_auth_headers()

    create_resp = requests.post(
        f"{base_url}/projects",
        json={"title": "Temp Project for Testing"},
        headers=headers,
    )
    assert (
        create_resp.status_code == 201
    ), f"Failed to create temp project: {create_resp.text}"

    project_id = create_resp.json().get("id")
    assert project_id, "API did not return project id in response"

    yield project_id

    requests.delete(f"{base_url}/projects/{project_id}", headers=headers)


def test_update_project_title_success(temp_project, base_url):
    """Позитивный тест: обновление названия существующего проекта"""
    new_title = f"Renamed Title {int(time.time())}"
    update_url = f"{base_url}/projects/{temp_project}"

    response = requests.put(
        update_url, json={"title": new_title}, headers=get_auth_headers()
    )

    assert (
        response.status_code == 200
    ), f"Expected 200 OK, got {response.status_code}. Body: {response.text}"
    resp_json = response.json()
    assert resp_json.get("title") == new_title
    assert resp_json.get("id") == temp_project


def test_update_project_without_auth_headers(base_url):
    """Негативный тест: отсутствие обязательных заголовков авторизации"""
    fake_uuid = str(uuid.uuid4())
    url = f"{base_url}/projects/{fake_uuid}"

    response = requests.put(url, json={"title": "No Auth"})

    assert response.status_code in (
        401,
        403,
    ), f"Unauthenticated request must be rejected. Got {response.status_code}"

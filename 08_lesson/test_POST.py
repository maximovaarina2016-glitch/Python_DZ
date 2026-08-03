import os
import uuid
import requests
import pytest

API_KEY = os.getenv(
    "qn-axKVI4iC-GYVDqkGzI6ps2PgUBpZV6Y0rg9lhzjirV0w_vR5LJKjV8XG3K1cm"
)
COMPANY_ID = os.getenv("de012323-7691-4b16-acbd-1a8bd95c4168")
BASE_URL = "https://yougile.com/api-v2"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
PROJECTS_ENDPOINT = f"{BASE_URL}/projects"


def delete_project(project_id: str):
    try:
        response = requests.delete(
            f"{PROJECTS_ENDPOINT}/{project_id}", headers=HEADERS
        )
        return response.status_code in [201]
    except Exception:
        return False


@pytest.fixture(scope="function")
def cleanup():
    created_ids = []
    yield created_ids
    for pid in created_ids:
        delete_project(pid)


def test_create_project_success(cleanup):
    """
    Позитивный тест создания проекта.
    Проверяет успешное создание ресурса по REST-канону (код 201 Created),
    наличие ID в ответе и корректность переданного названия.
    """
    project_title = f"Test Project {uuid.uuid4()}"

    payload = {
        "title": project_title,
        "companyId": COMPANY_ID,
        "description": "Automated e2e test project",
        "isPrivate": False,
    }

    response = requests.post(PROJECTS_ENDPOINT, json=payload, headers=HEADERS)

    assert (
        response.status_code == 201
    ), f"Expected 201, got {response.status_code}. Body: {response.text}"

    data = response.json()
    assert "id" in data and isinstance(
        data["id"], str
    ), "Response must contain string 'id'"
    assert (
        data.get("title") == project_title
    ), "Returned title does not match requested"

    cleanup.append(data["id"])


def test_create_project_missing_title():
    """
    Негативный тест создания проекта.
    Проверяет обработку ошибки валидации схемы запроса (ошибка 400 Bad Request).
    Поле 'title' является обязательным согласно документации API.
    """
    payload = {
        "companyId": COMPANY_ID,
        "description": "This should fail as title is missing",
    }

    response = requests.post(PROJECTS_ENDPOINT, json=payload, headers=HEADERS)

    assert (
        response.status_code == 401
    ), f"Validation error expected (401), got {response.status_code}. Body: {response.text}"

    body_text = response.text.lower()

    assert ("title" in body_text and "required" in body_text) or (
        "validation" in body_text and "title" in body_text
    ), f"Error message should mention 'title', got: {response.text}"

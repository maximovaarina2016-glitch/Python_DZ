import os
import uuid
import time
from dotenv import load_dotenv
import pytest
import requests

load_dotenv()

BASE_URL = os.getenv("YOUGILE_BASE_URL")
API_KEY = os.getenv("YOUGILE_API_KEY")
COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")

HEADERS = {
    "x-api-key": API_KEY,
    "companyId": COMPANY_ID,
    "Content-Type": "application/json",
}


@pytest.fixture(scope="function")
def temp_project():
    """
    Создает временный проект перед тестом и удаляет после.
    scope="function" гарантирует создание нового проекта для каждого теста.
    """
    project_name = (
        f"Test Project Auto {int(time.time())}_{uuid.uuid4().hex[:6]}"
    )

    create_url = f"{BASE_URL}/projects"
    payload = {
        "title": project_name,
        "description": "Project for automated tests",
    }

    response = requests.post(create_url, json=payload, headers=HEADERS)
    assert (
        response.status_code == 200
    ), f"Failed to setup test data: {response.text}"

    project_id = response.json()["id"]

    yield project_id

    delete_url = f"{BASE_URL}/projects/{project_id}"
    requests.delete(delete_url, headers=HEADERS)


@pytest.fixture(scope="function")
def created_project():
    """Создает реальный проект в Yougile и возвращает его ID и исходные данные."""
    unique_name = f"AT_Get_Project_{int(time.time())}_{uuid.uuid4().hex[:6]}"

    create_response = requests.post(
        f"{BASE_URL}/projects", json={"title": unique_name}, headers=HEADERS
    )
    assert (
        create_response.status_code == 200
    ), f"Сбой создания проекта: {create_response.text}"

    project_data = create_response.json()
    project_id = project_data["id"]

    yield project_id, project_data

    requests.delete(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)

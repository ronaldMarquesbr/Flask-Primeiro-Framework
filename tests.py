import pytest
import requests

url = "http://127.0.0.1:5000"
tasks = []


def test_create_task():
    new_task_data = {
        "title": "Titulo da descricao",
        "description": "Descricao da aula"
    }

    response = requests.post(f"{url}/tasks", json=new_task_data)
    assert response.status_code == 200

    response_json = response.json()

    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])


def test_get_tasks():
    response = requests.get(f"{url}/tasks")
    assert response.status_code == 200

    response_json = response.json()

    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{url}/tasks/{task_id}")

        assert response.status_code == 200

        response_json = response.json()

        assert response_json["id"] == task_id


def test_update_task():
    task_id = tasks[0]
    payload = {
        "title": "Novo titulo",
        "description": "Nova descricao",
        "completed": False
    }

    response = requests.put(f"{url}/tasks/{task_id}", json=payload)
    assert response.status_code == 200

    response_json = response.json()
    assert "message" in response_json

    # Confirmar dados com nova requisicao de verificacao
    response = requests.get(f"{url}/tasks/{task_id}")
    assert response.status_code == 200

    response_json = response.json()
    assert response_json["title"] == payload["title"]
    assert response_json["description"] == payload["description"]
    assert response_json["completed"] == payload["completed"]


def test_delete_task():
    if tasks:
        task_id = tasks[0]

        response = requests.delete(f"{url}/tasks/{task_id}")
        assert response.status_code == 200

        response = requests.get(f"{url}/tasks/{task_id}")
        assert response.status_code == 404

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_discipline_catalog_contains_all_four_domains() -> None:
    response = client.get("/api/disciplines")

    assert response.status_code == 200
    assert [item["id"] for item in response.json()] == [
        "mechanics",
        "optics",
        "electromagnetism",
        "thermology",
    ]


def test_ready_subject_has_structured_content() -> None:
    response = client.get("/api/subjects/dynamics")

    assert response.status_code == 200
    assert response.json()["animation"]["kind"] == "force-motion"
    assert response.json()["formulas"]


def test_unpublished_subject_returns_404() -> None:
    response = client.get("/api/subjects/kinematics")

    assert response.status_code == 404

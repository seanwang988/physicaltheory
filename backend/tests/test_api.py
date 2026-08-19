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


def test_statics_exposes_six_theory_pages() -> None:
    response = client.get("/api/subjects/statics/theories")

    assert response.status_code == 200
    theories = response.json()
    assert len(theories) == 6
    assert theories[0]["id"] == "force-composition"
    assert theories[-1]["id"] == "structural-equilibrium"


def test_every_statics_theory_has_complete_science_content() -> None:
    catalog = client.get("/api/subjects/statics/theories").json()

    for node in catalog:
        response = client.get(f"/api/theories/{node['id']}")
        assert response.status_code == 200
        detail = response.json()
        assert detail["formulas"]
        assert detail["experiment"]["kind"] == node["experiment_kind"]
        assert len(detail["applications"]) >= 3
        assert detail["scientists"]


def test_unknown_theory_returns_404() -> None:
    response = client.get("/api/theories/not-a-theory")

    assert response.status_code == 404

from app.app import app

def test_health_route():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data["status"] == "healthy"
    assert "container" in data
    assert "project" in data

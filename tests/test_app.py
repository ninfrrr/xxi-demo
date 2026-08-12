from app.main import app

def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Cinema XXI - Movie Info Service" in response.data

def test_movies_status_code():
    client = app.test_client()
    response = client.get("/movies")
    assert response.status_code == 200
    assert b"XXI" in response.data
    assert b"The Odyssey" in response.data
    assert b"Spider-Man: Brand New Day" in response.data

def test_movies_content():
    client = app.test_client()
    response = client.get("/movies")
    data = response.get_json()
    assert data["cinema"] == "XXI"
    assert len(data["now_showing"]) > 0

def test_health_status_code():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert b"ok" in response.data

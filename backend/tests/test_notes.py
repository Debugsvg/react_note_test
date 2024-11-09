import pytest
from test_react import main  # Importez l'application depuis le module correct

@pytest.fixture
def client():
    main.config['TESTING'] = True
    with main.test_client() as client:
        yield client

def test_get_notes(client):
    response = client.get('/notes')
    assert response.status_code == 200

def test_add_note(client):
    response = client.post('/addnotes', json={"title": "Test", "content": "Contenu de test"})
    assert response.status_code == 201

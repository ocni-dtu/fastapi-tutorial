def test_docs(client):
    response = client.get(f"/docs")

    assert response.status_code == 200

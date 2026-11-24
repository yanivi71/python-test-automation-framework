import requests


def test_get_post_returns_200(api_url):
    response = requests.get(f"{api_url}/posts/1")
    assert response.status_code == 200


def test_get_post_has_expected_fields(api_url):
    response = requests.get(f"{api_url}/posts/1")
    post = response.json()

    assert post["id"] == 1
    assert "title" in post
    assert "body" in post


def test_get_missing_post_returns_404(api_url):
    response = requests.get(f"{api_url}/posts/9999")
    assert response.status_code == 404

def test_create_post_returns_201(api_url):
    payload = {"title": "QA automation", "body": "testing", "userId": 1}

    response = requests.post(f"{api_url}/posts", json=payload)

    assert response.status_code == 201

    created = response.json()
    assert created["title"] == payload["title"]
    assert created["body"] == payload["body"]
    assert "id" in created
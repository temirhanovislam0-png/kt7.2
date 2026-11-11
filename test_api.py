import pytest
from api_client import *

def test_get_posts():
    response = get_posts()
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list) and len(posts) > 0
    assert {"id", "userId", "title", "body"} <= posts[0].keys()


@pytest.mark.parametrize("post_id", [1, 4, 67])
def test_get_post(post_id):
    response = get_post(post_id)
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    assert post["title"] and post["body"]


def test_create_post():
    response = create_post("Мой пост", "Текст поста", 1)
    assert response.status_code == 201
    post = response.json()
    assert post["title"] == "Мой пост"
    assert "id" in post


def test_not_exists_post():
    response = get_post(111)
    assert response.status_code == 404


def test_update_post():
    response = update_post(1, title="Новый", body="Новое тело", user_id=1)
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert post["title"] == "Новый"
    assert post["body"] == "Новое тело"


def test_patch_post():
    response = patch_post(3, title="Только заголовок")
    assert response.status_code == 200
    assert response.json()["title"] == "Только заголовок"


@pytest.mark.parametrize("post_id", [1, 50])
def test_delete_post(post_id):
    response = delete_post(post_id)
    assert response.status_code == 200
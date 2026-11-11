import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/'

def get_posts():
    return requests.get(f"{BASE_URL}/posts")

def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")

def get_posts_by_user(user_id):
    return requests.get(f"{BASE_URL}/posts", params={"userId": user_id})

def get_comments(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}/comments")

def create_post(title, body, user_id):
    return requests.post(f"{BASE_URL}/posts", json={
        "title": title, "body": body, "userId": user_id
    })

def _change_post(method, post_id, title=None, body=None, user_id=None):
    data = {}
    if title is not None:
        data["title"] = title
    if body is not None:
        data["body"] = body
    if user_id is not None:
        data["userId"] = user_id
    return requests.request(method, f"{BASE_URL}/posts/{post_id}", json=data)

def update_post(post_id, title=None, body=None, user_id=None):
    return _change_post("PUT", post_id, title, body, user_id)

def patch_post(post_id, title=None, body=None, user_id=None):
    return _change_post("PATCH", post_id, title, body, user_id)

def delete_post(post_id):
    return requests.delete(f"{BASE_URL}/posts/{post_id}")
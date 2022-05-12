def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data
    assert b'href="/about"' in response.data
    assert b'href="/welcome"' in response.data
    assert b'Index Page' in response.data


def test_auth_routes(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200
    response = client.get("/logout")
    assert response.status_code == 302
    response = client.get("/account")
    assert response.status_code == 200
    response = client.get("/profile")
    assert response.status_code == 200
    response = client.get("/users")
    assert response.status_code == 302
    response = client.get("/users/new")
    assert response.status_code == 302

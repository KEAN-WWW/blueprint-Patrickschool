"""Tests for homepage Blueprint routes."""


from application.app import init_app

def test_main_page_content():
    """Test that the homepage route returns status 200 and contains 'Blueprint'."""
    app = init_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Blueprint' in response.data

def test_about_page_content():
    """Test that the about route returns status 200 and contains 'Blueprint'."""
    app = init_app()
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200
    assert b'Blueprint' in response.data

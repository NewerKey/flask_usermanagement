"""
This file (test_users.py) contains the functional tests for the `users` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `users` blueprint.
"""


def test_login_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
    assert b'Email' in response.data
    assert b'Password' in response.data


def test_valid_login_logout(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login',
                                data=dict(email='john45@gmail.com', password='Somepassword'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for logging in, john45@gmail.com!' in response.data
    assert b'User Management System' in response.data
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'User Management System' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_invalid_login(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login',
                                data=dict(email='john45@gmail.com', password='Otherpassword'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'ERROR! Incorrect login credentials.' in response.data
    assert b'User Management System' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_login_already_logged_in(test_client, init_database, login_default_user):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST) when the user is already logged in
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login',
                                data=dict(email='john45@gmail.com', password='Otherpassword'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Already logged in!  Redirecting to your User Profile page...' in response.data
    assert b'User Management System' in response.data
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data


def test_valid_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_client.post('/register',
                                data=dict(email='lizzy80@gmail.com',
                                          password='Anotherpassword',
                                          confirm='Anotherpassword'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, lizzy80@gmail.com!' in response.data
    assert b'User Management System' in response.data
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data

    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Goodbye!' in response.data
    assert b'User Management System' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_invalid_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/register',
                                data=dict(email='pat70@yahoo.com',
                                          password='Thepassword',
                                          confirm='Thepassword2'),   # Does NOT match!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Thanks for registering, pat70@yahoo.com!' not in response.data
    assert b'[This field is required.]' not in response.data
    assert b'User Management System' in response.data
    assert b'Logout' not in response.data
    assert b'Login' in response.data
    assert b'Register' in response.data


def test_duplicate_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST) using an email address already registered
    THEN check an error message is returned to the user
    """
    # Register the new account
    test_client.post('/register',
                     data=dict(email='jp20@hotmail.com',
                               password='Strongpassword',
                               confirm='Strongpassword'),
                     follow_redirects=True)
    # Try registering with the same email address
    response = test_client.post('/register',
                                data=dict(email='jp20@hotmail.com',
                                          password='Strongerpassword',
                                          confirm='Strongerpassword'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Already registered!  Redirecting to your User Profile page...' in response.data
    assert b'Thanks for registering, jp20@hotmail.com!' not in response.data
    assert b'User Management System' in response.data
    assert b'Logout' in response.data
    assert b'Login' not in response.data
    assert b'Register' not in response.data

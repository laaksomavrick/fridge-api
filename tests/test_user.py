from flask import url_for
from faker import Faker

fake = Faker()


class TestUser:

    def test_it_succeeds_creating_a_user(self, app):
        url = url_for('user.create_user')
        resp = app.post_json(url, {
            'username': fake.first_name(),
            'email': fake.ascii_email(),
            'password': 'password',
            'passwordConfirmation': 'password'
        })
        assert resp.status_int == 200
        assert 'id' in resp.json

    def test_it_fails_when_password_confirmation_wrong(self, app):
        url = url_for('user.create_user')
        resp = app.post_json(url, {
            'username': fake.first_name(),
            'email': fake.ascii_email(),
            'password': 'password',
            'passwordConfirmation': 'something else'
        }, expect_errors=True)
        assert resp.status_int == 422

    def test_it_fails_when_user_already_exists(self, app):
        url = url_for('user.create_user')
        username = fake.first_name()
        app.post_json(url, {
            'username': username,
            'email': fake.ascii_email(),
            'password': 'password',
            'passwordConfirmation': 'password'
        })
        resp = app.post_json(url, {
            'username': username,
            'email': fake.ascii_email(),
            'password': 'password',
            'passwordConfirmation': 'password'
        }, expect_errors=True)
        assert resp.status_int == 422

    def test_it_succeeds_logging_in_a_user(self, app):
        create_user_url = url_for('user.create_user')
        login_user_url = url_for('user.login_user')
        username = fake.first_name()
        password = 'password'
        app.post_json(create_user_url, {
            'username': username,
            'email': fake.ascii_email(),
            'password': password,
            'passwordConfirmation': password
        })
        resp = app.post_json(login_user_url, {
            'username': username,
            'password': password
        })
        assert resp.status_int == 200
        assert 'accessToken' in resp.json

    def test_it_fails_logging_in_a_user_when_user_doesnt_exist(self, app):
        login_user_url = url_for('user.login_user')
        username = fake.first_name()
        password = 'password'
        resp = app.post_json(login_user_url, {
            'username': username,
            'password': password
        }, expect_errors=True)
        assert resp.status_int == 404

    def test_it_fails_logging_in_a_user_when_password_is_wrong(self, app):
        create_user_url = url_for('user.create_user')
        login_user_url = url_for('user.login_user')
        username = fake.first_name()
        password = 'password'
        app.post_json(create_user_url, {
            'username': username,
            'email': fake.ascii_email(),
            'password': password,
            'passwordConfirmation': password
        })
        resp = app.post_json(login_user_url, {
            'username': username,
            'password': 'a wrong password'
        }, expect_errors=True)
        assert resp.status_int == 401
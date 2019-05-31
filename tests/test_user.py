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
        assert resp.status_int == 400

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

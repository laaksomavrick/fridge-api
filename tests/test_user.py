from flask import url_for
from faker import Faker

fake = Faker()

class TestUser:

    def test_it_can_create_a_user(self, testapp):
        url = url_for('user.create_user')
        resp = testapp.post_json(url, {
            'username': fake.first_name(),
            'email': fake.ascii_email(),
            'password': 'password',
            'passwordConfirmation': 'password'
        })
        assert resp.status_int == 200
        assert 'id' in resp.json
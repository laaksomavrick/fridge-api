import pytest
from webtest import TestApp

from fridge.app import create_app
from fridge.extensions import db as _db


@pytest.fixture(scope='function')
def test_app():
    """An application for the tests."""
    _app = create_app()

    with _app.app_context():
        _db.create_all()

    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()
    with _app.app_context():
        meta = _db.metadata
        for table in reversed(meta.sorted_tables):
            print('Truncating table {}'.format(table))
            _db.session.execute(table.delete())
        _db.session.commit()


@pytest.fixture(scope='function')
def app(test_app):
    """A Webtest app."""
    return TestApp(test_app)

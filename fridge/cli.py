import click
from faker import Faker
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from fridge.extensions import db
from fridge.sticky.models import Sticky
from fridge.user.models import User
from fridge.utils import truncate_tables


@click.command("seed")
@with_appcontext
def seed():
    print("Seeding database.")
    truncate_tables(current_app, db)
    fake = Faker()

    username = fake.user_name()
    user = User(username=username, email=fake.free_email())
    user.set_password('password')
    print('Generating user: {}'.format(username))

    user.stickies = []
    for _ in range(5):
        sticky = Sticky(
            title=fake.sentence(),
            content=fake.paragraph()
        )
        user.stickies.append(sticky)
    print("Generating stickies.")

    db.session.add(user)
    db.session.commit()

    print("Database seeded.")

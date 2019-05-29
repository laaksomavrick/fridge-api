from fridge.extensions import db

class Sticky(db.Model):
    __tablename__ = 'stickies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Sticky {}>'.format(self.title)

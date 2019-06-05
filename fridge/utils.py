def truncate_tables(app, db):
    with app.app_context():
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print('Truncating table {}'.format(table))
            db.session.execute(table.delete())
        db.session.commit()
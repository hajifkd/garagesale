from garage import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)
    note = db.Column(db.Text)
    price = db.Column(db.Integer)
    photo_data = db.Column(db.Text) # base64 encoded - ugly



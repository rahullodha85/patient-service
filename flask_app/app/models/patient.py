from flask_app.app import db


class patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publid_id = db.Column(db.String, unique=True)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    email = db.Column(db.String(120), unique=True)
    phonenumber = db.Column(db.String(20))
    address = db.Column(db.Text)

    def __str__(self):
        return self.email
from app import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(20))
    address = db.Column(db.Text)

    def __str__(self):
        return self.email

    def serialize(self):
        return {
            'id': self.public_id,
            'first-name': self.first_name,
            'last-name': self.last_name,
            'email': self.email,
            'phone-number': self.phone_number,
            'address': self.address
        }


# This is for GUS
class Trades(db.Model):
    Product = db.Column(db.String(20))
    Reference = db.Column(db.String(20), primary_key=True)
    ProviderAction = db.Column(db.String(20))

    def serialize(self):
        return {
            'Product': self.Product,
            'Reference #': self.Reference,
            'Provider Action': self.ProviderAction
        }

from init import db, ma, Marshmallow
from marshmallow import fields

class Card(db.Model):
    __tablename__ ="cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(db.Text))
    status = db.Column(db.String)
    date = db.Column(db.Date) # the date the card was created
    status = db.Column(db.String)
    priority = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeinKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='cards')


class CardSchema(ma.schema):
    user = fields.Nested('UserSchema', only = ['name', 'email'])
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'date', 'status', 'priority', 'user')

card_schema = CardSchema()
cards_schema = CardSchema(many=True)
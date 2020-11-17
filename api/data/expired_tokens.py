from flask_mongoengine import Document
from mongoengine import StringField

class ExpiredTokens(Document):
    token = StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'expired_tokens'
    }
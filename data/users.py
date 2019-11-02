from datetime import datetime
from mongoengine import Document, BooleanField, StringField, EmailField, BinaryField, DateTimeField, ListField, IntField


class User(Document):
    active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    name = StringField(required=True)
    email = EmailField(unique=True, required=True)
    password = BinaryField(required=True)
    registered_datetime = DateTimeField(default=datetime.utcnow)

    post_ids = ListField(IntField)
    comments_ids = ListField(IntField)

    meta = {
        'db_alias': 'core',
        'collection': 'users',
        'indexes': ['name', 'email'],
        'ordering': ['-registered_datetime']
    }

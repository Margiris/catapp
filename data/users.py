from datetime import datetime
from json import dumps
from flask_mongoengine import Document
from mongoengine import BooleanField, StringField, EmailField, BinaryField, DateTimeField, ListField, ReferenceField, LazyReferenceField


class Users(Document):
    active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    name = StringField(required=True)
    email = EmailField(unique=True, required=True)
    password = BinaryField(required=True)
    registered_datetime = DateTimeField(default=datetime.utcnow)

    posts = ListField(ReferenceField('Posts'))
    comments = ListField(ReferenceField('Comments'))

    def to_json(self):
        user_dict = {
            'status': 'active' if self.active else 'banned',
            'is_admin': self.is_admin,
            'name': self.name,
            'email': self.email,
            'registered on': str(self.registered_datetime.replace(microsecond=0)),
            'user post count': len(self.posts),
            'comment count': len(self.comments)
        }
        return dumps(user_dict)

    meta = {
        'db_alias': 'core',
        'collection': 'users',
        'indexes': ['name', 'email'],
        'ordering': ['-registered_datetime']
    }

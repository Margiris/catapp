from datetime import datetime

from flask_mongoengine import Document
from mongoengine import BooleanField, StringField, EmailField, BinaryField, DateTimeField, ListField, ReferenceField


class Users(Document):
    active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    name = StringField(unique=True)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
    registered_datetime = DateTimeField(default=datetime.utcnow)

    posts = ListField(ReferenceField('Posts'))
    comments = ListField(ReferenceField('Comments'))

    def to_json(self):
        return {
            'status': 'active' if self.active else 'banned',
            'is_admin': self.is_admin,
            'name': self.name,
            'email': self.email,
            'registered_on': str(self.registered_datetime.replace(microsecond=0)),
            'user_post_count': len(self.posts),
            'comment_count': len(self.comments)
        }

    meta = {
        'db_alias': 'core',
        'collection': 'users',
        'indexes': ['name', 'email'],
        'ordering': ['-registered_datetime']
    }

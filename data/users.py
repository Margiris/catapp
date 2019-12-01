from datetime import datetime
from flask_mongoengine import Document
from mongoengine import BooleanField, StringField, EmailField, BinaryField, DateTimeField, ListField, ReferenceField, LazyReferenceField


class Users(Document):
    active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    name = StringField(primary_key=True)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
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
        return user_dict

    meta = {
        'db_alias': 'core',
        'collection': 'users',
        'indexes': ['email'],
        'ordering': ['-registered_datetime']
    }

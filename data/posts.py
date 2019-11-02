from datetime import datetime
from mongoengine import Document, StringField, FileField, DateTimeField, ReferenceField, IntField, EmbeddedDocumentListField
from data.users import User
from data.comments import Comment
from data.ratings import Rating


class Post(Document):
    title = StringField(required=True)
    image_path = FileField(required=True)
    posted_datetime = DateTimeField(default=datetime.utcnow)
    op_id = ReferenceField(User)

    comments = EmbeddedDocumentListField(Comment)
    rating = EmbeddedDocumentListField(Rating)

    meta = {
        'db_alias': 'core',
        'collection': 'posts',
        'indexes': ['title'],
        'ordering': ['-posted_datetime']
    }

from datetime import datetime
from mongoengine import Document, StringField, FileField, DateTimeField, ReferenceField, EmbeddedDocumentListField


class Posts(Document):
    title = StringField(required=True)
    image_path = FileField(required=True)
    posted_datetime = DateTimeField(default=datetime.utcnow)
    op_id = ReferenceField('Users')

    comments = EmbeddedDocumentListField('Comments')
    rating = EmbeddedDocumentListField('Ratings')

    meta = {
        'db_alias': 'core',
        'collection': 'posts',
        'indexes': ['title'],
        'ordering': ['-posted_datetime']
    }

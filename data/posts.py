from datetime import datetime
from json import dumps

from flask_mongoengine import Document
from mongoengine import StringField, ImageField, DateTimeField, ReferenceField, EmbeddedDocumentListField, EmbeddedDocumentField, CASCADE
from PIL import PILLOW_VERSION


class Posts(Document):
    title = StringField(required=True)
    image = ImageField(required=True, thumbnail_size=(400, 400, True))
    posted_datetime = DateTimeField(default=datetime.utcnow)
    author = ReferenceField('Users', reverse_delete_rule=CASCADE)

    comments = EmbeddedDocumentListField('Comments')
    rating = EmbeddedDocumentField('Ratings')

    def to_json(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'posted on': str(self.posted_datetime.replace(microsecond=0)),
            'by': self.author.name,
            'comment count': len(self.comments),
            'score': self.rating.score
        }

    meta = {
        'db_alias': 'core',
        'collection': 'posts',
        'indexes': ['title'],
        'ordering': ['-posted_datetime']
    }

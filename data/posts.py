from datetime import datetime
from json import dumps

from flask_mongoengine import Document
from mongoengine import StringField, ImageField, DateTimeField, ReferenceField, EmbeddedDocumentListField
from PIL import PILLOW_VERSION


class Posts(Document):
    title = StringField(required=True)
    image = ImageField(required=True, thumbnail_size=(400, 400, True))
    posted_datetime = DateTimeField(default=datetime.utcnow)
    author = ReferenceField('Users')

    comments = EmbeddedDocumentListField('Comments')
    rating = EmbeddedDocumentListField('Ratings')

    def to_json(self):
        post_dict = {
            'id': str(self.id),
            'title': self.title,
            'posted on': str(self.posted_datetime.replace(microsecond=0)),
            'by': self.author,
            'comment count': len(self.comments),
            # TODO get score value instead of ratings object
            'score': self.rating
        }
        return post_dict

    meta = {
        'db_alias': 'core',
        'collection': 'posts',
        'indexes': ['title'],
        'ordering': ['-posted_datetime']
    }

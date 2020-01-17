from datetime import datetime
from bson.objectid import ObjectId

from mongoengine import EmbeddedDocument, ObjectIdField, DateTimeField, ReferenceField, StringField, EmbeddedDocumentField


class Comments(EmbeddedDocument):
    id = ObjectIdField(default=ObjectId, primary_key=True)
    posted_datetime = DateTimeField(default=datetime.utcnow)
    author = ReferenceField('Users')
    body = StringField(required=True)
    rating = EmbeddedDocumentField('Ratings')

    def to_json(self):
        try:
            author = self.author.name
        except:
            author = "[deleted]"
        return {
            'id': str(self.id),
            'posted_time': str(self.posted_datetime.replace(microsecond=0)),
            'author': author,
            'body': self.body,
            'rating': self.rating.score
        }

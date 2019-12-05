from datetime import datetime

from mongoengine import EmbeddedDocument, DateTimeField, ReferenceField, StringField, EmbeddedDocumentField


class Comments(EmbeddedDocument):
    posted_datetime = DateTimeField(default=datetime.utcnow)
    author = ReferenceField('Users')
    body = StringField(required=True)
    rating = EmbeddedDocumentField('Ratings')

from datetime import datetime
from mongoengine import EmbeddedDocument, DateTimeField, StringField, EmbeddedDocumentListField


class Comments(EmbeddedDocument):
    posted_datetime = DateTimeField(default=datetime.utcnow)
    body = StringField(required=True)
    rating = EmbeddedDocumentListField('Ratings')

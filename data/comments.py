from datetime import datetime
from mongoengine import EmbeddedDocument, DateTimeField, StringField, EmbeddedDocumentListField

from data.ratings import Rating


class Comment(EmbeddedDocument):
    posted_datetime = DateTimeField(default=datetime.utcnow)
    body = StringField()
    rating = EmbeddedDocumentListField(Rating)

from mongoengine import EmbeddedDocument, IntField


class Rating(EmbeddedDocument):
    upvote_count = IntField()
    downvote_count = IntField()

    @property
    def score(self):
        return self.upvote_count - self.downvote_count

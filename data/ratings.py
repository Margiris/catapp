from mongoengine import EmbeddedDocument, IntField


class Ratings(EmbeddedDocument):
    upvote_count = IntField()
    downvote_count = IntField()

    @property
    def score(self):
        return self.upvote_count - self.downvote_count

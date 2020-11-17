from mongoengine import EmbeddedDocument, IntField


class Ratings(EmbeddedDocument):
    upvote_count = IntField(min_value=0, default=0)
    downvote_count = IntField(min_value=0, default=0)

    @property
    def score(self):
        return self.upvote_count - self.downvote_count

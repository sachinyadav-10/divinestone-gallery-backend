from mongoengine import Document
from mongoengine import StringField


class Health(Document):
    name = StringField(required=True)

    meta = {
        "collection": "health",
    }
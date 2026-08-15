from django.utils import timezone

from mongoengine import BooleanField
from mongoengine import DateTimeField
from mongoengine import Document
from mongoengine import StringField


class BaseDocument(Document):
    meta = {
        "abstract": True,
        "db_alias": "default",
    }

    created_at = DateTimeField(default=timezone.now)
    updated_at = DateTimeField(default=timezone.now)

    created_by = StringField()
    updated_by = StringField()

    is_active = BooleanField(default=True)
    is_deleted = BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def soft_delete(self):
        self.is_deleted = True
        self.is_active = False
        self.updated_at = timezone.now()
        self.save()
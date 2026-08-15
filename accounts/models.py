from mongoengine import (
    DateTimeField,
    EmailField,
    StringField,
)

from django.utils import timezone

from common.base_model import BaseDocument


class User(BaseDocument):
    # -----------------------------
    # Basic Information
    # -----------------------------
    full_name = StringField(
        required=True,
        max_length=100,
    )

    email = EmailField(
        required=True,
        unique=True,
    )

    password = StringField(
        required=True,
    )

    phone = StringField(
        max_length=20,
    )

    # -----------------------------
    # Role
    # -----------------------------
    role = StringField(
        default="Admin",
        choices=[
            "Super Admin",
            "Admin",
        ],
    )

    # -----------------------------
    # Authentication
    # -----------------------------
    last_login = DateTimeField()

    meta = {
        "collection": "users",
        "db_alias": "default",
        "indexes": [
            {
                "fields": ["email"],
                "unique": True,
            },
            "role",
            "is_active",
        ],
        "ordering": [
            "full_name",
        ],
    }

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()

    def __str__(self):
        return self.full_name
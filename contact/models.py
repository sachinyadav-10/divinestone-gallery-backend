from mongoengine import (
    EmailField,
    StringField,
)

from common.base_model import BaseDocument


class Contact(BaseDocument):
    # -----------------------------
    # Customer Information
    # -----------------------------
    name = StringField(
        required=True,
        max_length=100,
    )

    email = EmailField(
        required=True,
    )

    phone = StringField(
        required=True,
        max_length=20,
    )

    city = StringField(
        max_length=100,
    )

    # -----------------------------
    # Inquiry Information
    # -----------------------------
    subject = StringField(
        required=True,
        max_length=200,
    )

    message = StringField(
        required=True,
        max_length=5000,
    )

    preferred_contact = StringField(
        default="Phone",
        choices=[
            "Phone",
            "Email",
            "WhatsApp",
        ],
    )

    product = ReferenceField(
        Product,
        required=False,
    )

    # -----------------------------
    # Status
    # -----------------------------
    status = StringField(
        default="Open",
        choices=[
            "Open",
            "In Progress",
            "Resolved",
            "Closed",
        ],
    )

    # -----------------------------
    # Internal Notes
    # -----------------------------
    admin_notes = StringField()

    meta = {
        "collection": "contacts",
        "db_alias": "default",
        "indexes": [
            "email",
            "phone",
            "status",
            "created_at",
            "is_active",
        ],
        "ordering": [
            "-created_at",
        ],
    }

    def __str__(self):
        return f"{self.name} ({self.subject})"
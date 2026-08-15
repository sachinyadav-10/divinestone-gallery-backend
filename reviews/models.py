from mongoengine import (
    BooleanField,
    EmailField,
    FloatField,
    IntField,
    ReferenceField,
    StringField,
)

from common.base_model import BaseDocument
from products.models import Product


class Review(BaseDocument):
    # -----------------------------
    # Product Reference
    # -----------------------------
    product = ReferenceField(
        Product,
        required=True,
    )

    # -----------------------------
    # Customer Details
    # -----------------------------
    customer_name = StringField(
        required=True,
        max_length=100,
    )

    email = EmailField(
        required=True,
    )

    city = StringField(
        max_length=100,
    )

    # -----------------------------
    # Review Details
    # -----------------------------
    rating = FloatField(
        required=True,
        min_value=1,
        max_value=5,
    )

    title = StringField(
        required=True,
        max_length=150,
    )

    review = StringField(
        required=True,
        max_length=3000,
    )

    verified_purchase = BooleanField(
        default=False,
    )

    # -----------------------------
    # Review Status
    # -----------------------------
    status = StringField(
        default="Pending",
        choices=[
            "Pending",
            "Approved",
            "Rejected",
        ],
    )

    # -----------------------------
    # Meta
    # -----------------------------
    meta = {
        "collection": "reviews",
        "db_alias": "default",
        "indexes": [
            "product",
            "status",
            "rating",
            "created_at",
            "is_active",
        ],
        "ordering": [
            "-created_at",
        ],
    }

    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"
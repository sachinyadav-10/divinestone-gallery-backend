from mongoengine import (
    EmailField,
    FloatField,
    IntField,
    ReferenceField,
    StringField,
)

from common.base_model import BaseDocument
from products.models import Product


class Booking(BaseDocument):
    # -----------------------------
    # Booking Information
    # -----------------------------
    booking_number = StringField(
        required=True,
        unique=True,
        max_length=30,
    )

    # -----------------------------
    # Customer Information
    # -----------------------------
    customer_name = StringField(
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

    # -----------------------------
    # Address
    # -----------------------------
    address = StringField(
        required=True,
    )

    city = StringField(
        required=True,
        max_length=100,
    )

    state = StringField(
        required=True,
        max_length=100,
    )

    country = StringField(
        default="India",
        max_length=100,
    )

    pincode = StringField(
        required=True,
        max_length=10,
    )

    # -----------------------------
    # Product Information
    # -----------------------------
    product = ReferenceField(
        Product,
        required=True,
    )

    quantity = IntField(
        default=1,
        min_value=1,
    )

    # -----------------------------
    # Price Snapshot
    # -----------------------------
    product_name = StringField(
        required=True,
        max_length=200,
    )

    product_price = FloatField(
        required=True,
        min_value=0,
    )

    total_amount = FloatField(
        required=True,
        min_value=0,
    )

    currency = StringField(
        default="INR",
        max_length=10,
    )

    # -----------------------------
    # Customer Message
    # -----------------------------
    message = StringField()

    # -----------------------------
    # Payment
    # -----------------------------
    payment_status = StringField(
        default="Pending",
        choices=[
            "Pending",
            "Paid",
            "Partially Paid",
            "Refunded",
        ],
    )

    # -----------------------------
    # Booking Status
    # -----------------------------
    booking_status = StringField(
        default="New",
        choices=[
            "New",
            "Contacted",
            "Confirmed",
            "In Production",
            "Ready To Dispatch",
            "Dispatched",
            "Delivered",
            "Cancelled",
        ],
    )

    # -----------------------------
    # Internal Admin Notes
    # -----------------------------
    admin_notes = StringField()

    meta = {
        "collection": "bookings",
        "db_alias": "default",
        "indexes": [
            {
                "fields": ["booking_number"],
                "unique": True,
            },
            "customer_name",
            "phone",
            "booking_status",
            "payment_status",
            "created_at",
            "product",
        ],
        "ordering": [
            "-created_at",
        ],
    }

    def __str__(self):
        return self.booking_number
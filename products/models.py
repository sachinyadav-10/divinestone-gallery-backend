from mongoengine import (
    BooleanField,
    DateTimeField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
    FloatField,
    IntField,
    ListField,
    ReferenceField,
    StringField,
    URLField,
)

from common.base_model import BaseDocument

from django.utils import timezone

class ProductImage(EmbeddedDocument):
    image_url = URLField(
        required=True
    )

    alt_text = StringField(
        max_length=200
    )

    display_order = IntField(
        default=1
    )

    is_primary = BooleanField(
        default=False
    )

class ProductFeature(EmbeddedDocument):
    title = StringField(
        required=True,
        max_length=100
    )

    display_order = IntField(
        default=1
    )

class CareInstruction(EmbeddedDocument):
    instruction = StringField(
        required=True,
        max_length=300
    )

    display_order = IntField(
        default=1
    )

class Product(BaseDocument):
    # -----------------------------
    # Basic Information
    # -----------------------------
    name = StringField(
        required=True,
        unique=True,
        max_length=200,
    )

    slug = StringField(
        required=True,
        unique=True,
        max_length=220,
    )

    short_description = StringField(
        max_length=500,
    )

    description = StringField()

    # -----------------------------
    # Category
    # -----------------------------
    category = ReferenceField(
        Category,
        required=True,
    )

    # -----------------------------
    # Pricing
    # -----------------------------
    price = FloatField(
        required=True,
        min_value=0,
    )

    discount_price = FloatField(
        min_value=0,
        default=None,
        null=True,
    )

    currency = StringField(
        default="INR",
        max_length=10,
    )

    # -----------------------------
    # Material
    # -----------------------------
    material = StringField(
        required=True,
        max_length=100,
    )

    color = StringField(
        max_length=100,
    )

    finish = StringField(
        max_length=100,
    )

    # -----------------------------
    # Dimensions
    # -----------------------------
    height = FloatField(
        min_value=0,
    )

    width = FloatField(
        min_value=0,
    )

    depth = FloatField(
        min_value=0,
    )

    weight = FloatField(
        min_value=0,
    )

    dimension_unit = StringField(
        default="inch",
        max_length=20,
    )

    weight_unit = StringField(
        default="kg",
        max_length=20,
    )

    # -----------------------------
    # Images
    # -----------------------------
    images = EmbeddedDocumentListField(
        ProductImage,
        default=list,
    )

    # -----------------------------
    # Features
    # -----------------------------
    features = EmbeddedDocumentListField(
        ProductFeature,
        default=list,
    )

    # -----------------------------
    # Care Instructions
    # -----------------------------
    care_instructions = EmbeddedDocumentListField(
        CareInstruction,
        default=list,
    )

    # -----------------------------
    # Availability
    # -----------------------------
    availability = StringField(
        default="Made To Order",
        choices=[
            "In Stock",
            "Made To Order",
            "Out Of Stock",
        ],
    )

    estimated_delivery_days = IntField(
        default=15,
        min_value=1,
    )

    # -----------------------------
    # Ratings
    # -----------------------------
    average_rating = FloatField(
        default=0.0,
    )

    total_reviews = IntField(
        default=0,
    )

    # -----------------------------
    # Product Flags
    # -----------------------------
    is_featured = BooleanField(
        default=False,
    )

    is_customizable = BooleanField(
        default=False,
    )

    # -----------------------------
    # SEO
    # -----------------------------
    seo_title = StringField(
        max_length=120,
    )

    seo_description = StringField(
        max_length=300,
    )

    seo_keywords = ListField(
        StringField(max_length=50),
        default=list,
    )

    # -----------------------------
    # Meta
    # -----------------------------
    meta = {
        "collection": "products",
        "db_alias": "default",
        "indexes": [
            {
                "fields": ["slug"],
                "unique": True,
            },
            "category",
            "price",
            "discount_price",
            "material",
            "availability",
            "is_featured",
            "is_active",
            "created_at",
            "average_rating",
        ],
        "ordering": [
            "-created_at",
        ],
    }

    def __str__(self):
        return self.name



class Category(BaseDocument):
    name = StringField(
        required=True,
        unique=True,
        max_length=100,
    )

    slug = StringField(
        required=True,
        unique=True,
        max_length=120,
    )

    description = StringField()

    thumbnail = URLField()

    banner_image = URLField()

    display_order = IntField(default=0)

    is_featured = BooleanField(default=False)

    seo_title = StringField(max_length=120)

    seo_description = StringField(max_length=300)

    seo_keywords = StringField()

    meta = {
        "collection": "categories",
        "db_alias": "default",
        "indexes": [
            {
                "fields": ["slug"],
                "unique": True,
            },
            "name",
            "display_order",
            "is_featured",
            "is_active",
        ],
        "ordering": [
            "display_order",
            "name",
        ],
    }

    def __str__(self):
        return self.name
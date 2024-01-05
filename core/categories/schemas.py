from typing import Optional
from uuid import UUID
from ninja import Schema, ModelSchema

from core.categories.models import Category


class CategoryCreate(Schema):
    name: str
    parent: Optional[UUID] = None


class CategoryOutWithoutParent(Schema):
    uuid: UUID
    name: str


class CategoryOut(ModelSchema):
    parent: Optional[CategoryOutWithoutParent] = None
    children: Optional[list[CategoryOutWithoutParent]] = None

    class Meta:
        model = Category
        fields = '__all__'
        count = None


class CategoryUpdate(Schema):
    name: Optional[str] = None
    parent: Optional[UUID] = None


class CategoryFilters(Schema):
    name: Optional[str] = None
    parent: Optional[UUID] = None

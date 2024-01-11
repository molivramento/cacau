from typing import Optional
from uuid import UUID
from ninja import Schema, ModelSchema
from core.categories.models import Category


class CategoryCreate(Schema):
    name: str
    parent_id: Optional[UUID] = None


class CategoryOut(ModelSchema):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryUpdate(Schema):
    name: Optional[str] = None
    parent: Optional[UUID] = None


class CategoryFilters(Schema):
    name: Optional[str] = None
    name__icontains: Optional[str] = None
    parent: Optional[UUID] = None
    parent__isnull: Optional[bool] = None
    parent__name: Optional[str] = None

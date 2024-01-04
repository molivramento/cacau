from typing import Optional
from uuid import UUID
from typing_extensions import Annotated

from ninja import Schema
from pydantic import field_validator

from core.categories.models import Category


class CategoryCreate(Schema):
    name: str
    parent: Optional[UUID] = None


class CategoryOut(Schema):
    uuid: UUID
    name: str
    parent: Optional[UUID] = None
    children: Optional[list['CategoryOut']] = None

    @classmethod
    @field_validator('children')
    def load_children(cls, v, values):
        if 'uuid' in values:
            return Category.objects.filter(parent=values['uuid'])
        return v


class CategoryUpdate(Schema):
    name: Optional[str] = None
    parent: Optional[UUID] = None


class CategoryFilters(Schema):
    name: Optional[str] = None
    parent: Optional[UUID] = None
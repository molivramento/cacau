from typing import Optional
from uuid import UUID

from ninja import Schema


class CategoryCreate(Schema):
    name: str
    parent: Optional[UUID] = None


class CategoryOut(Schema):
    uuid: UUID
    name: str
    parent: Optional['CategoryOut'] = None


class CategoryUpdate(Schema):
    name: Optional[str] = None
    parent: Optional[UUID] = None


class CategoryFilters(Schema):
    name: Optional[str] = None
    parent: Optional[UUID] = None
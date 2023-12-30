from typing import Optional
from uuid import UUID
from ninja import Schema


class ProductAttributeCreate(Schema):
    name: str
    tag: str
    unity: str


class ProductAttributeOut(ProductAttributeCreate):
    uuid: UUID


class ProductAttributeUpdate(Schema):
    name: Optional[str] = None
    tag: Optional[str] = None
    unity: Optional[str] = None


class ProductAttributeFilters(Schema):
    name: Optional[str] = None
    name__icontains: Optional[str] = None
    tag: Optional[str] = None
    tag__icontains: Optional[str] = None

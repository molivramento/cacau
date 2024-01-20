from uuid import UUID

from ninja import Router, Query
from core.products_stock.manager import product_stock_manager
from core.products_stock.schemas import ProductStockOut, ProductStockCreate, ProductStockUpdate, ProductStockFilter

router = Router()


@router.get('', response=list[ProductStockOut])
def list_product_stock(request, filters: Query[ProductStockFilter]):
    return product_stock_manager.get_all(filters)


@router.get('{uuid}', response=ProductStockOut)
def get_product_stock(request, uuid: UUID):
    return product_stock_manager.get(uuid)


@router.post('', response=ProductStockOut)
def create_product_stock(request, product_stock: ProductStockCreate):
    return product_stock_manager.create(product_stock)


@router.put('{uuid}', response=ProductStockUpdate)
def update_product_stock(request, uuid: UUID, product_stock: ProductStockUpdate):
    return product_stock_manager.update(uuid, product_stock)


@router.delete('{uuid}')
def delete_product_stock(request, uuid: UUID):
    return product_stock_manager.delete(uuid)

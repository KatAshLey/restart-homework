#initialize Inventory Item
from pydantic import BaseModel, field_validator
from .ItemOrigin import ItemOrigin

#initialize Inventory item class
class InventoryItem(BaseModel):
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin
    
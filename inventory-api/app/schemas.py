from pydantic import BaseModel
from typing import Optional
from datetime import date
from datetime import datetime

class SupplierBase(BaseModel):
    name: str
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class SupplierOut(SupplierBase):
    supplier_id: int

    class Config:
        orm_mode = True




class CategoryBase(BaseModel):
    category_name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    category_id: int

    class Config:
        orm_mode = True




class UserBase(BaseModel):
    username: str
    email: str
    role: Optional[str] = 'clerk'

class UserCreate(UserBase):
    password_hash: str  # In real apps, you'd hash this

class UserOut(UserBase):
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True



# Schema for creating a new customer
class CustomerCreate(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

# Schema for returning a customer (e.g., from DB)
class Customer(CustomerCreate):
    customer_id: int

    class Config:
        orm_mode = True




# Schema for creating a new stock entry
class StockEntryCreate(BaseModel):
    product_id: int
    supplier_id: int
    quantity: int
    entry_date: Optional[date] = None
    user_id: Optional[int] = None

# Schema for returning a stock entry
class StockEntry(StockEntryCreate):
    entry_id: int

    class Config:
        orm_mode = True



class StockMovementBase(BaseModel):
    product_id: int
    quantity_change: int
    movement_type: str  # Should be 'IN' or 'OUT'
    user_id: Optional[int] = None

class StockMovementCreate(StockMovementBase):
    pass

class StockMovement(StockMovementBase):
    movement_id: int
    movement_date: datetime

    class Config:
        orm_mode = True
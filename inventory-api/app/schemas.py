from pydantic import BaseModel
from typing import Optional

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
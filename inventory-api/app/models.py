from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, ForeignKey, Enum, DECIMAL, Date
from sqlalchemy.orm import relationship
from database.connection import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(30), default="clerk")
    created_at = Column(TIMESTAMP)

    stock_entries = relationship("StockEntry", back_populates="user")
    stock_movements = relationship("StockMovement", back_populates="user")


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    contact_person = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(Text)

    products = relationship("Product", back_populates="supplier")
    stock_entries = relationship("StockEntry", back_populates="supplier")


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"))
    quantity_in_stock = Column(Integer, default=0)
    unit_price = Column(DECIMAL(10, 2))
    created_at = Column(TIMESTAMP)

    category = relationship("Category", back_populates="products")
    supplier = relationship("Supplier", back_populates="products")
    stock_entries = relationship("StockEntry", back_populates="product")
    stock_movements = relationship("StockMovement", back_populates="product")


class StockEntry(Base):
    __tablename__ = "stock_entries"

    entry_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    entry_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    product = relationship("Product", back_populates="stock_entries")
    supplier = relationship("Supplier", back_populates="stock_entries")
    user = relationship("User", back_populates="stock_entries")


class StockMovement(Base):
    __tablename__ = "stock_movements"

    movement_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    quantity_change = Column(Integer, nullable=False)
    movement_type = Column(Enum('IN', 'OUT'), nullable=False)
    movement_date = Column(TIMESTAMP)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    product = relationship("Product", back_populates="stock_movements")
    user = relationship("User", back_populates="stock_movements")


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(Text)

from pydantic import BaseModel

# Common user fields
class UserBase(BaseModel):
    name: str
    email: str

# For creating new users
class UserCreate(UserBase):
    password: str

# For updating users (optional extension)
class UserUpdate(UserBase):
    pass

# Response model
class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # updated from orm_mode

# ✅ Login schema - used for login endpoint
class UserLogin(BaseModel):
    email: str
    password: str

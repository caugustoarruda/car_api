from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict, field_validator
from datetime import datetime


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator('username')
    def username_min_length(cls, field):
        if len(field) < 3:
            raise ValueError('Username deve ter pelo menos 3 caracteres')
        return field
    
    @field_validator('password')
    def password_min_length(cls, field):
        if len(field) < 3:
            raise ValueError('Password deve ter pelo menos 3 caracteres')
        return field


class UserPublicSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime



class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    @field_validator('username')
    def username_min_length(cls, field):
        if len(field) < 3:
            raise ValueError('Username deve ter pelo menos 3 caracteres')
        return field
    
    @field_validator('password')
    def password_min_length(cls, field):
        if len(field) < 3:
            raise ValueError('Password deve ter pelo menos 3 caracteres')
        return field


class UserListPublicSchema(BaseModel):
    users: List[UserPublicSchema]
    offset: int
    limit: int
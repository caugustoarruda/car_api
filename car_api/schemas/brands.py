from pydantic import BaseModel, field_validator, ConfigDict
from datetime import datetime
from typing import Optional, List


class BrandSchema(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True

    @field_validator('name')
    def name_min_length(cls, field):
        if len(field) < 3:
            raise ValueError('Nome da marca deve ter pelo menos 2 caracteres')
        

class BrandUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

    @field_validator('name')
    def name_min_length(cls, field):
        if len(field) < 3:
            raise ValueError('Nome da marca deve ter pelo menos 2 caracteres')
        

class BrandPublicSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime


class BrandListSchema(BaseModel):
    brands: List[BrandPublicSchema]
    offset: int
    limit: int
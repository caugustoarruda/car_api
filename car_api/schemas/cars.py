from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, field_validator

from car_api.models.cars import TransmissionType, FuelType
from car_api.schemas.brands import BrandPublicSchema
from car_api.schemas.users import UserPublicSchema


class CarSchema(BaseModel):
    mode: str
    factory_year: int
    model_year: int
    color: str
    plate: str
    fuel_type: FuelType
    transmission_type: TransmissionType
    price: Decimal
    description: Optional[str] = None
    is_available: bool = True
    brand_id: int
    owner_id: int

    @field_validator('model')
    def model_min_length(cls, field):
        if len(field.strip()) < 2:
            raise ValueError('Modelo deve ter pelo menos 2 caracteres')
        
        return field.strip()
    
    @field_validator('color')
    def color_min_length(cls, field):
        if len(field.strip()) < 2:
            raise ValueError('Color deve ter pelo menos 2 caracteres')
        
        return field.strip()
    
    @field_validator('plate')
    def plate_format(cls, field):
        plate = field.strip()
        if len(plate) < 7 or len(plate) > 10:
            raise ValueError('Placa deve ter entre 7 e 10 caracteres')
        return plate
    
    @field_validator('factory_year', 'model_year')
    def year_validation(cls, field):
        if field < 1900 or field > 2030:
            raise ValueError('Ano deve estar entre 1900 e 2030')
        return field
    
    @field_validator('price')
    def price_validation(cls, field):
        if field <= 0:
            raise ValueError('Preço deve ser maior que zero')
        return field



class CarUpdateSchema(BaseModel):
    model: Optional[str] = None
    factory_year: Optional[int] = None
    model_year: Optional[int] = None
    color: Optional[str] = None
    plate: Optional[str] = None
    fuel_type: Optional[FuelType] = None
    transmission: Optional[TransmissionType] = None
    price: Optional[Decimal] = None
    description: Optional[str] = None
    is_available: Optional[bool] = None
    brand_id: Optional[int] = None
    owner_id: Optional[int] = None

        @field_validator('model')
    def model_min_length(cls, field):
        if len(field.strip()) < 2:
            raise ValueError('Modelo deve ter pelo menos 2 caracteres')
        
        return field.strip()
    
    @field_validator('color')
    def color_min_length(cls, field):
        if len(field.strip()) < 2:
            raise ValueError('Color deve ter pelo menos 2 caracteres')
        
        return field.strip()
    
    @field_validator('plate')
    def plate_format(cls, field):
        plate = field.strip()
        if len(plate) < 7 or len(plate) > 10:
            raise ValueError('Placa deve ter entre 7 e 10 caracteres')
        return plate
    
    @field_validator('factory_year', 'model_year')
    def year_validation(cls, field):
        if field < 1900 or field > 2030:
            raise ValueError('Ano deve estar entre 1900 e 2030')
        return field
    
    @field_validator('price')
    def price_validation(cls, field):
        if field <= 0:
            raise ValueError('Preço deve ser maior que zero')
        return field


class CarPublicSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    model: str
    factory_year: int
    model_year: int
    color: str
    plate: str
    fuel_type: FuelType
    transmission: TransmissionType
    price: Decimal
    description: Optional[str]
    is_available: bool
    brand_id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime]
    brand: BrandPublicSchema
    owner: UserPublicSchema


class CarListPublicSchema(BaseModel):
    cars: List[CarPublicSchema]
    offset: int
    limit: int    
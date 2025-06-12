from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Base schema for Animal creation
class AnimalCreate(BaseModel):
    nome: str
    sexo: int
    raca: int
    data_nascimento: datetime
    status: int

# Schema for Animal updates
class AnimalUpdate(BaseModel):
    nome: Optional[str] = None
    sexo: Optional[int] = None
    raca: Optional[int] = None
    data_nascimento: Optional[datetime] = None
    status: Optional[int] = None

# Schema for Animal response
class AnimalResponse(BaseModel):
    id: int
    nome: str
    sexo: int
    raca: int
    data_nascimento: datetime
    status: int
    
    class Config:
        from_attributes = True

# Schema for vaccination records
class VacinacaoCreate(BaseModel):
    animal_id: int
    nome: str
    data: datetime

class VacinacaoResponse(BaseModel):
    id: int
    animal_id: int
    nome: str
    data: datetime
    
    class Config:
        from_attributes = True

# Schema for weight records
class PesagemCreate(BaseModel):
    id_animal: int
    peso: float
    data: datetime

class PesagemResponse(BaseModel):
    id: int
    id_animal: int
    peso: float
    data: datetime
    
    class Config:
        from_attributes = True

class MessageResponse(BaseModel):
    message: str

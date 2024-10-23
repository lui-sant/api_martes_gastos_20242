from pydantic import BaseModel,Field
from datetime import date


#los DTO son clase que establecen 
#el modelo de transferencia de datos

class UsuarioDTOPeticion(BaseModel):
    nombres:str
    fechaDeNacimiento:date
    ubicacion:str
    metaAhorro:float
    class Config:
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id:int
    nombres:str
    metaAhorros:float
    class Config:
        orm_mode=True


class GastoDTOPeticion(BaseModel):
    valor:float
    descripcion:str
    fecha:date
    class Config:
        orm_mode=True

class GastoDTORespuesta(BaseModel):
    id:int  
    descripcion:str
    valor:float
    class Config:
        orm_mode=True



class CategoriaDTOPeticion(BaseModel):
    nombre:str
    descripcion:str
    fotoCategoria:str
    class Config:
        orm_mode=True

class CategoriaDTORespuesta(BaseModel):
   id:int
   descripcion:str
   fotoCategoria:str
   class Config:
        orm_mode=True

class IngresoDTOPeticion(BaseModel):
    valor:float
    descripcion:str
    fecha:date
    class Config:
        orm_mode=True
        
class IngresoDTORespuesta(BaseModel):
    valor:float
    descripcion:str
    fecha:date
    class Config:
        orm_mode=True

        
    
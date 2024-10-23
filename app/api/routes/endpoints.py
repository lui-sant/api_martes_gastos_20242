from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import UsuarioDTOPeticion,UsuarioDTORespuesta
from app.api.DTO.dtos import GastoDTOPeticion,GastoDTORespuesta
from app.api.DTO.dtos import CategoriaDTOPeticion,CategoriaDTORespuesta
from app.api.DTO.dtos import IngresoDTOPeticion,IngresoDTORespuesta
from app.api.models.tablasSQL import Usuario
from app.api.models.tablasSQL import Gasto
from app.api.models.tablasSQL import Categoria
from app.api.models.tablasSQL import Ingreso
from app.database.configuration import SessionLocal,engine

rutas=APIRouter()

#conexion a la base de datos
def conectarConBd():
    try:
        baseDatos=SessionLocal()
        yield baseDatos
    except Exception as error:
        baseDatos.rollback()
        raise error

    finally:
        baseDatos.close()


#construllendo nuestros servicios

#Cada servicio (operacion o  transaccion en BD)debe programar como funcion
@rutas.post("/usuario", response_model=UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos")
def guardarUsuario(datosUsuario:UsuarioDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        usuario=Usuario(
            nombres=datosUsuario.nombres,
            fechaDeNacimiento=datosUsuario.fechaDeNacimiento,
            ubicacion=datosUsuario.ubicacion,
            mataDeAhorro=datosUsuario.metaAhorro
        )
        #ordenandole a  la base de datos
        database.add(usuario)
        database.commit()
        database.refresh(usuario)
        return usuario

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")
    


@rutas.get("/usuario", response_model=List[UsuarioDTORespuesta],summary="Buscar todos los usuarios en BD")    
def buscarUsuario(database:Session=Depends(conectarConBd)):

    try:
        usuarios=database.query(Usuario).all()
        return usuarios

    except Exception as error:
        database.rollback
        raise HTTPException(status_code=400,detail=f"No se puede buscar los usuarios {error}")
    


#GASTOS POST
@rutas.post("/gasto", response_model=GastoDTORespuesta, summary="Registrar un gasto en la base de datos")
def guardarGasto(datosGasto:GastoDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        gasto=Gasto(
            descripcion=datosGasto.descripcion,
            valor=datosGasto.valor,
            fecha=datosGasto.fecha,
          
        )
        #ordenandole a  la base de datos
        database.add(gasto)
        database.commit()
        database.refresh(gasto)
        return gasto

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")



#GASTOS GET    
@rutas.get("/gasto", response_model=List[GastoDTORespuesta],summary="Buscar todos los gastos en BD")    
def buscarGasto(database:Session=Depends(conectarConBd)):

    try:
        gastos=database.query(Gasto).all()
        return gastos

    except Exception as error:
        database.rollback
        raise HTTPException(status_code=400,detail=f"No se puede buscar los gastos {error}") 


#CATEGORIA POST
@rutas.post("/categoria", response_model=CategoriaDTORespuesta, summary="Registrar una categoria en la base de datos")
def guardarCategoria(datosCategoria:CategoriaDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        categoria=Categoria(
            nombre=datosCategoria.nombre,
            descripcion=datosCategoria.descripcion,
            fotoCategoria=datosCategoria.fotoCategoria
          
        )
        #ordenandole a  la base de datos
        database.add(categoria)
        database.commit()
        database.refresh(categoria)
        return categoria

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}") 



#CATEGORIA GET    
@rutas.get("/categoria", response_model=List[CategoriaDTORespuesta],summary="Buscar todas las categorias en BD")    
def buscarCategoria(database:Session=Depends(conectarConBd)):

    try:
        categoria=database.query(Categoria).all()
        return categoria

    except Exception as error:
        database.rollback
        raise HTTPException(status_code=400,detail=f"No se puede buscar los gastos {error}") 



#INGRESO POST
@rutas.post("/ingreso", response_model=IngresoDTORespuesta, summary="Registrar un ingreso en la base de datos")
def guardarIngreso(datosIngreso:IngresoDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        ingreso=Ingreso(
            valor=datosIngreso.valor,
            descripcion=datosIngreso.descripcion,
            fecha=datosIngreso.fecha
          
        )
        #ordenandole a  la base de datos
        database.add(ingreso)
        database.commit()
        database.refresh(ingreso)
        return ingreso

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400,detail=f"Tenemos un problema {error}")  


#INGRESO GET
@rutas.get("/ingreso", response_model=List[IngresoDTORespuesta],summary="Buscar todos los ingresos en BD")    
def buscarIngreso(database:Session=Depends(conectarConBd)):

    try:
        ingreso=database.query(Ingreso).all()
        return ingreso

    except Exception as error:
        database.rollback
        raise HTTPException(status_code=400,detail=f"No se puede buscar los ingresos {error}") 
                 


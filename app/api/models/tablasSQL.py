from sqlalchemy import Column, Integer,String,Float,Date,ForeignKey

from sqlalchemy.orm import relationship


from sqlalchemy.ext.declarative import declarative_base


#llamado a la base para crear tablas
Base=declarative_base()

#definicion de las tablas de mi modelo


#usuario
class Usuario(Base):
    __tablename__='usuario'
    id=Column(Integer, primary_key=True,autoincrement=True)
    nombres=Column(String(50))
    fechaDeNacimiento=Column(Date)
    ubicacion=Column(String(100))
    mataDeAhorro=Column(Float)

#gasto
class Gasto(Base):
    __tablename__='gasto'
    id=Column(Integer, primary_key=True,autoincrement=True)
    descripcion=Column(String(50))
    #categoria*****
    valor=Column(Integer)
    fecha=Column (Date)
    
#categoria

class Categoria(Base):
    __tablename__='categoria'
    id=Column(Integer, primary_key=True,autoincrement=True)
    nombre=Column(String(50))
    descripcion=Column(String(100))
    fotoCategoria=Column(String(200))  
    
#ingreso

class Ingreso(Base):
    __tablename__='ingreso'
    id=Column(Integer, primary_key=True,autoincrement=True)
    valor=Column(Integer)
    descripcion=Column(String(50))
    fecha=Column (Date)
    
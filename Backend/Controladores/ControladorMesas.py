from Repositorios.RepositorioMesas import RepositorioMesas
from Modelos.Mesas import Mesas
class ControladorMesas():
    def __init__(self):
        self.repositorioMesas = RepositorioMesas()
    def index(self):
        return self.repositorioMesas.findAll()
    def create(self,infoMesas):
        nuevoMesas=Mesas(infoMesas)
        return self.repositorioMesas.save(nuevoMesas)
    def show(self,id):
        elMesas=Mesas(self.repositorioMesas.findById(id))
        return elMesas.__dict__
    def update(self,id,infoMesas):
        MesasActual=Mesas(self.repositorioMesas.findById(id))
        MesasActual.cedula=infoMesas["cedula"]
        MesasActual.nombre = infoMesas["nombre"]
        MesasActual.apellido = infoMesas["apellido"]
        return self.repositorioMesas.save(MesasActual)
    def delete(self,id):
        return self.repositorioMesas.delete(id)

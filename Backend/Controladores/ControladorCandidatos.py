from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Repositorios.RepositorioPartidos import RepositorioPartidos
from Modelos.Candidatos import Candidatos
from Modelos.Partidos import Partidos
class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()
        self.repositorioPartidos = RepositorioPartidos()
    def index(self):
        return self.repositorioCandidatos.findAll()
    def create(self,infoCandidatos):
        nuevoCandidatos=Candidatos(infoCandidatos)
        return self.repositorioCandidatos.save(nuevoCandidatos)
    def show(self,id):
        elCandidatos=Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidatos.__dict__
    def update(self,id,infoCandidatos):
        CandidatosActual=Candidatos(self.repositorioCandidatos.findById(id))
        CandidatosActual.nombre=infoCandidatos["nombre"]
        CandidatosActual.creditos = infoCandidatos["creditos"]
        return self.repositorioCandidatos.save(CandidatosActual)
    def delete(self,id):
        return self.repositorioCandidatos.delete(id)
    """
    Relación Partidos y Candidatos
    """
    def asignarPartidos(self, id, id_Partidos):
        CandidatosActual = Candidatos(self.repositorioCandidatos.findById(id))
        PartidosActual = Partidos(self.repositorioPartidos.findById(id_Partidos))
        CandidatosActual.Partidos = PartidosActual
        return self.repositorioCandidatos.save(CandidatosActual)


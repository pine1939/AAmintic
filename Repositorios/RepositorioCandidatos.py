from bson import ObjectId
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Candidatos import Candidatos
class RepositorioCandidatos(InterfaceRepositorio[Candidatos]):
    def getListadoMateriasEnPartidos(self, id_candidatos):
        theQuery = {"partidos.$id": ObjectId(id_candidatos)}
        return self.query(theQuery)
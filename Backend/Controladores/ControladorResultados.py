from Modelos.Resultados import Resultados
from Modelos.Mesas import Mesas
from Modelos.Candidatos import Candidatos
from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioMesas import RepositorioMesas
from Repositorios.RepositorioCandidatos import RepositorioCandidatos
class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()
        self.repositorioMesass = RepositorioMesas()
        self.repositorioCandidatoss = RepositorioCandidatos()
    def index(self):
        return self.repositorioResultados.findAll()
    """
    Asignacion Mesas y Candidatos a inscripción
    """
    def create(self,infoResultados,id_Mesas,id_Candidatos):
        nuevaResultados=Resultados(infoResultados)
        elMesas=Mesas(self.repositorioMesass.findById(id_Mesas))
        laCandidatos=Candidatos(self.repositorioCandidatoss.findById(id_Candidatos))
        nuevaResultados.Mesas=elMesas
        nuevaResultados.Candidatos=laCandidatos
        return self.repositorioResultados.save(nuevaResultados)
    def show(self,id):
        elResultados=Resultados(self.repositorioResultados.findById(id))
        return elResultados.__dict__
    """
    Modificación de inscripción (Mesas y Candidatos)
    """
    def update(self,id,infoResultados,id_Mesas,id_Candidatos):
        laResultados=Resultados(self.repositorioResultados.findById(id))
        laResultados.año=infoResultados["año"]
        laResultados.semestre = infoResultados["semestre"]
        laResultados.notaFinal=infoResultados["nota_final"]
        elMesas = Mesas(self.repositorioMesass.findById(id_Mesas))
        laCandidatos = Candidatos(self.repositorioCandidatoss.findById(id_Candidatos))
        laResultados.Mesas = elMesas
        laResultados.Candidatos = laCandidatos
        return self.repositorioResultados.save(laResultados)
    def delete(self, id):
        return self.repositorioResultados.delete(id)
    "Obtener todos los inscritos en una Candidatos"
    def listarInscritosEnCandidatos(self,id_Candidatos):
        return self.repositorioResultados.getListadoInscritosEnCandidatos(id_Candidatos)
    "Obtener notas mas altas por curso"
    def notasMasAltasPorCurso(self):
        return self.repositorioResultados.getMayorNotaPorCurso()
    "Obtener promedio de notas en Candidatos"
    def promedioNotasEnCandidatos(self,id_Candidatos):
        return self.repositorioResultados.promedioNotasEnCandidatos(id_Candidatos)

    def test(self,id_Candidatos):
        return self.repositorioResultados.test(id_Candidatos)

from Repositorios.RepositorioPartidos import RepositorioPartidos
from Modelos.Partidos import Partidos
from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Repositorios.RepositorioResultados import RepositorioResultados
class ControladorPartidos():
    def __init__(self):
        self.repositorioPartidos = RepositorioPartidos()
        self.repositorioCandidatos = RepositorioCandidatos()
        self.repositorioResultados = RepositorioResultados()
    def index(self):
        return self.repositorioPartidos.findAll()
    def create(self,infoPartidos):
        nuevoPartidos=Partidos(infoPartidos)
        return self.repositorioPartidos.save(nuevoPartidos)
    def show(self,id):
        elPartidos=Partidos(self.repositorioPartidos.findById(id))
        return elPartidos.__dict__
    def update(self,id,infoPartidos):
        PartidosActual=Partidos(self.repositorioPartidos.findById(id))
        PartidosActual.nombre=infoPartidos["nombre"]
        PartidosActual.descripcion = infoPartidos["descripcion"]
        return self.repositorioPartidos.save(PartidosActual)
    def delete(self,id):
        return self.repositorioPartidos.delete(id)
    def getCandidatoss(self,idCandidatos):
        return self.repositorioCandidatos.getListadoCandidatossEnPartidos(idCandidatos)
    def getPromedioGeneral(self,idPartidos):
        elPartidos = self.repositorioPartidos.findById(idPartidos)
        elPartidos["Candidatos"]=self.repositorioCandidatos.getListadoCandidatossEnPartidos(idPartidos)
        suma=0
        contador=0
        i=0
        for CandidatosActual in elPartidos["Candidatos"]:
            listadoInscritos=self.repositorioResultados.getListadoInscritosEnCandidatos(CandidatosActual["_id"])
            elPartidos["Candidatoss"][i]["inscritos"]=listadoInscritos
            i+=1
            for ResultadosActual in listadoInscritos:
                suma += ResultadosActual["nota_final"]
                contador+=1

        promedio=suma/contador
        elPartidos["promedio_notas"]=promedio
        return elPartidos


from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados

from bson import ObjectId

class RepositorioResultados(InterfaceRepositorio[Resultados]):
    def getListadoInscritosEnCandidatos(self, id_candidatos):
        theQuery = {"candidato.$id": ObjectId(id_candidatos)}
        return self.query(theQuery)
    def getMayorNotaPorVotacion(self):## recordar para el controlador ----------------------------------- resultados-candidato
        query1={
                "$group": {
                    "_id": "$candidatos",
                    "max": {
                        "$max": "$votacion_final"
                    },
                    "doc": {
                        "$first": "$$ROOT"
                    }
                }
            }
        pipeline=  [query1]
        return self.queryAggregation(pipeline)
    def promedioVotacionEnCandidatos(self,id_candidatos):
        query1 = {
          "$match": {"candidatos.$id": ObjectId(id_candidatos)}
        }
        query2 = {
          "$group": {
            "_id": "$candidatos",
            "promedio": {
              "$avg": "$votacion_final"
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)
    def test(self,id_materia):
        query1 = {
          "$match": {"materia.$id": ObjectId(id_materia)}
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)


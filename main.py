from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorMesas import ControladorMesas
from Controladores.ControladorPartidos import ControladorPartidos
from Controladores.ControladorCandidatos import ControladorCandidatos
from Controladores.ControladorResultados import ControladorResultados
miControladorMesas=ControladorMesas()
miControladorPartidos=ControladorPartidos()
miControladorCandidatos=ControladorCandidatos()
miControladorResultados=ControladorResultados()
###################################################################################
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
###################################################################################
@app.route("/Mesass",methods=['GET'])
def getMesass():
    json=miControladorMesas.index()
    return jsonify(json)
@app.route("/Mesass",methods=['POST'])
def crearMesas():
    data = request.get_json()
    json=miControladorMesas.create(data)
    return jsonify(json)
@app.route("/Mesass/<string:id>",methods=['GET'])
def getMesas(id):
    json=miControladorMesas.show(id)
    return jsonify(json)
@app.route("/Mesass/<string:id>",methods=['PUT'])
def modificarMesas(id):
    data = request.get_json()
    json=miControladorMesas.update(id,data)
    return jsonify(json)
@app.route("/Mesass/<string:id>",methods=['DELETE'])
def eliminarMesas(id):
    json=miControladorMesas.delete(id)
    return jsonify(json)
###################################################################################
@app.route("/Partidoss",methods=['GET'])
def getPartidoss():
    json=miControladorPartidos.index()
    return jsonify(json)
@app.route("/Partidoss/<string:id>",methods=['GET'])
def getPartidos(id):
    json=miControladorPartidos.show(id)
    return jsonify(json)

@app.route("/Partidoss/<string:id>/Candidatoss",methods=['GET'])
def getCandidatossPartidos(id):
    json=miControladorPartidos.getCandidatoss(id)
    return jsonify(json)

@app.route("/Partidoss",methods=['POST'])
def crearPartidos():
    data = request.get_json()
    json=miControladorPartidos.create(data)
    return jsonify(json)
@app.route("/Partidoss/<string:id>",methods=['PUT'])
def modificarPartidos(id):
    data = request.get_json()
    json=miControladorPartidos.update(id,data)
    return jsonify(json)
@app.route("/Partidoss/<string:id>",methods=['DELETE'])
def eliminarPartidos(id):
    json=miControladorPartidos.delete(id)
    return jsonify(json)
@app.route("/Partidoss/<string:id>/promedio",methods=['GET'])
def promedioPartidos(id):
    json=miControladorPartidos.getPromedioGeneral(id)
    return jsonify(json)
###################################################################################
@app.route("/Candidatoss",methods=['GET'])
def getCandidatoss():
    json=miControladorCandidatos.index()
    return jsonify(json)
@app.route("/Candidatoss/<string:id>",methods=['GET'])
def getCandidatos(id):
    json=miControladorCandidatos.show(id)
    return jsonify(json)
@app.route("/Candidatoss",methods=['POST'])
def crearCandidatos():
    data = request.get_json()
    json=miControladorCandidatos.create(data)
    return jsonify(json)
@app.route("/Candidatoss/<string:id>",methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json=miControladorCandidatos.update(id,data)
    return jsonify(json)
@app.route("/Candidatoss/<string:id>",methods=['DELETE'])
def eliminarCandidatos(id):
    json=miControladorCandidatos.delete(id)
    return jsonify(json)
@app.route("/Candidatoss/<string:id>/Partidos/<string:id_Partidos>",methods=['PUT'])
def asignarPartidosACandidatos(id,id_Partidos):
    json=miControladorCandidatos.asignarPartidos(id,id_Partidos)
    return jsonify(json)
###################################################################################
@app.route("/Resultadoses",methods=['GET'])
def getResultadoses():
    json=miControladorResultados.index()
    return jsonify(json)
@app.route("/Resultadoses/<string:id>",methods=['GET'])
def getResultados(id):
    json=miControladorResultados.show(id)
    return jsonify(json)
@app.route("/Resultadoses/Mesas/<string:id_Mesas>/Candidatos/<string:id_Candidatos>",methods=['POST'])
def crearResultados(id_Mesas,id_Candidatos):
    data = request.get_json()
    json=miControladorResultados.create(data,id_Mesas,id_Candidatos)
    return jsonify(json)
@app.route("/Resultadoses/<string:id_Resultados>/Mesas/<string:id_Mesas>/Candidatos/<string:id_Candidatos>",methods=['PUT'])
def modificarResultados(id_Resultados,id_Mesas,id_Candidatos):
    data = request.get_json()
    json=miControladorResultados.update(id_Resultados,data,id_Mesas,id_Candidatos)
    return jsonify(json)
@app.route("/Resultadoses/<string:id_Resultados>",methods=['DELETE'])
def eliminarResultados(id_Resultados):
    json=miControladorResultados.delete(id_Resultados)
    return jsonify(json)
@app.route("/Resultadoses/Candidatos/<string:id_Candidatos>",methods=['GET'])
def inscritosEnCandidatos(id_Candidatos):
    json=miControladorResultados.listarInscritosEnCandidatos(id_Candidatos)
    return jsonify(json)
@app.route("/Resultadoses/notas_mayores",methods=['GET'])
def getNotasMayores():
    json=miControladorResultados.notasMasAltasPorCurso()
    return jsonify(json)
@app.route("/Resultadoses/promedio_notas/Candidatos/<string:id_Candidatos>",methods=['GET'])
def getPromedioNotasEnCandidatos(id_Candidatos):
    json=miControladorResultados.promedioNotasEnCandidatos(id_Candidatos)
    return jsonify(json)
###################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

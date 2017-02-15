from flask import Flask, abort, redirect, jsonify, request
from flask_migrate import Migrate
from config import *	
from models import *

db.create_all()

@app.route("/api/municipio", methods=['GET'])
def municipios():
	valores=[]
	listamunicipios = Municipio.query.all()
	for und in listamunicipios:
		municipios = {
			"cod_municipio": und.cod_municipio,
			"descricao": und.descricao
		}
		valores.append(municipios)
	return jsonify(valores)

@app.route("/api/municipio/<int:cod_municipio>", methods=['GET'])
def municipio(cod_municipio):
	valores=[]
	listamunicipios = Municipio.query.filter(Municipio.cod_municipio == cod_municipio).all()
	for und in listamunicipios:
		municipio = {
			"cod_municipio": und.cod_municipio,
			"descricao": und.descricao
		}
		valores.append(municipio)
	return jsonify(valores)

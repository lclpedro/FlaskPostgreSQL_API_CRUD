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
	listamunicipios = Municipio.query.filter(Municipio.cod_municipio == cod_municipio)
	for und in listamunicipios:
		municipio = {
			"cod_municipio": und.cod_municipio,
			"descricao": und.descricao
		}
		valores.append(municipio)
	return jsonify(valores)

@app.route("/api/municipio/<int:cod_municipio>", methods=['DELETE'])
def deletar_municipio(cod_municipio):
	municipio = Municipio.query.filter(Municipio.cod_municipio == cod_municipio).first()
	db.session.delete(municipio)
	db.session.commit()

	msg = "Deletado com sucesso!"
	return msg

@app.route("/api/municipio", methods=['POST'])
def inserir_municipio():
	descricao = request.json.get('descricao')

	municipio = {
		'descricao':descricao
	}

	addMunicipio = Municipio(**municipio)
	db.session.add(addMunicipio)
	db.session.commit()

	msg = "Inserido com sucesso!"
	return msg

@app.route("/api/municipio/<int:cod_municipio>", methods=['PUT'])
def atualizar_municipio(cod_municipio):
	valores = request.json

	Municipio.query.filter(Municipio.cod_municipio == cod_municipio).update(valores)
	db.session.commit()
	msg = "Estado atualizado com sucesso!"	
	return msg
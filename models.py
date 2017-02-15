from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import db

class Estado(db.Model):
	__tablename__ ='estado'
	cod_estado = db.Column(db.Integer(), primary_key=True)
	uf = db.Column(db.String(2), unique=True)

class Municipio(db.Model):
	__tablename__ ='municipio'
	cod_municipio = db.Column(db.Integer(), primary_key=True)
	descricao = db.Column(db.String(80))
	cod_estado = db.Column(db.Integer(), db.ForeignKey('estado.cod_estado'))
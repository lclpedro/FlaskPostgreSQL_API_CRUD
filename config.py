from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask("gpro")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/teste'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = 'KjgVgytVJuUYfkjgUYHGCF'
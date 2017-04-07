# Aplicação Python FLASK - API CRUD

A aplicação foi desenvolvida com o intuito de ajudar os programadores python que estão iniciando, utilizando flask. 

Requisitos mínimos:
  - Python 3.5.2
  - PostgreSQL
  - Flask (apenas instalar o requirements.txt que funciona)

### Um pouco do que eu desenvolvi
No início encontrei muita dificuldade para poder utilizar o flask, até mesmo para criar, e desenvolver APIs que seja utilizadas no dia a dia, então com base nessas dificuldades resolvi disponibilizar essa API, para levar como base na produção de um sistema maior, e com isso poder fluir mais na área.


### Utilização da API
1. Instalar o python 3.5.2
1.1 Clonar o projeto
2. Depois de clonar o projeto, com seu prompt de comando localize a pasta do projeto e vamos instalar o virtualenv.
```sh
$ pip install virtualenv
```
3. Vamos criar um ambiente para esse projeto.
```sh
$ virtualenv env
```
4. Agora é hora de habiliar o env, dentro da pasta do projeto pode verificar que a pasta env foi criada, para ativar ela digite no seu prompt de comando. 
```sh
$ env\Script\activate
```
5. instalar dependecias
```sh	
(env) pip install -r requirements.txt 
```
6. Criar o banco de dados.
6.1 Entre no pgadmin e crie um database com o nome 'teste'
> Lembrando que precisa ter o PostgreSQL instalado.

7. Executar a aplicação
```sh
(env) python run.py
```
Se tudo der certo irá aparecer.
```sh
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Depois que estiver funcionando, atravez do postman é só fazer os testes atraves do postman.


Obrigado! 
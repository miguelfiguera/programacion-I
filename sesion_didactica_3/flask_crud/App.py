from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

#inicializar Flask App.
app = Flask (__name__)
#clave secreta
app.app_context()
app.secret_key='RackhamCalicoJack'

#configuracion de la base de datos y del ORM
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db=SQLAlchemy(app)

#clase para guardar datos y modelar datos:

class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200))
    description=db.Column(db.String(500))
    complete=db.Column(db.Boolean)
    create_at=db.Column(db.DateTime, default=db.func.current_timestamp())
    

with app.app_context():
    db.create_all()

#Ruta principal de la app
@app.route('/')


#Funcion que renderiza el index.html
def index():
    tasks=Task.query.all()
    return render_template('index.html',list_tasks=tasks)



@app.route('/create-task',methods=['POST'])
def create_task():
    new_task=Task(title=request.form['task_title'],description=request.form['task_description'],complete=False,create_at=db.func.current_timestamp())
    db.session.add(new_task)
    db.session.commit()
    return index()


#Debug activado.
if __name__ == "__main__":
    app.run(debug=True)




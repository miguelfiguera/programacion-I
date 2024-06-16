from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

#inicializar Flask App.
app = Flask (__name__)
#clave secreta
app.app_context()
app.secret_key='RackhamCalicoJack'

#configuracion de la base de datos y del ORM
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
db=SQLAlchemy(app)

#clase para modelar datos:
class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200))
    description=db.Column(db.String(500))
    complete=db.Column(db.Boolean)
    create_at=db.Column(db.DateTime, default=db.func.current_timestamp())
    

#Creacion de la base de datos con los modelos correspondientes.
with app.app_context():
    db.create_all()

#Ruta principal de la app
@app.route('/')


#Funcion que renderiza el index.html
def index():
    tasks=Task.query.all()
    return render_template('index.html',list_tasks=tasks)


#define la ruta para crear tareas
@app.route('/create-task',methods=['POST'])
#define la funcion para crear tareas
def create_task():
    new_task=Task(title=request.form['task_title'],description=request.form['task_description'],complete=False,create_at=db.func.current_timestamp())
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

#define la ruta y la funcion para borrar tareas
@app.route('/delete/<id>')
def delete_task(id):
    Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('index'))


#define la funcion para actualizar tareas a complete==True exclusivamente.
@app.route('/update/<id>')
def update_task(id):
    task=Task.query.filter_by(id=int(id)).first()
    task.complete=True
    db.session.commit()
    return redirect(url_for('index'))


#define la ruta para editar titulo y texto de la tarea en un form renderizado en la ruta edit.
@app.route('/edit/<id>')
def edit_page(id):
    task=Task.query.filter_by(id=int(id)).first()
    return render_template('edit.html',task=task)


#define la ruta para actualizar la base de datos y la funcion con los nuevos datos del formulario de /edit/<id>
@app.route('/edit-task/<id>',methods=['POST'])
def edit_task(id):
    task=Task.query.filter_by(id=int(id)).first()
    task.title=request.form['task_title_edit']
    task.description=request.form['task_description_edit']
    db.session.commit()
    return redirect(url_for('index'))


#Debug activado.
if __name__ == "__main__":
    app.run(debug=True)




from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre}


tareas = [
    {'id': 1, 'nombre': 'comprar pan'},
    {'id': 2, 'nombre': 'comprar azúcar'}
]

@app.route('/')
def home(): 
    return 'Hola, Flask'

@app.route('/api/tareas', methods=['GET'])
def get_tareas():
    return jsonify(tareas)

@app.route('/api/tareas', methods=['POST'])
def add_tareas(): 
    nueva_tarea = request.json
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201
 
@app.route('/api/tareas/<int:id>', methods=['DELETE'])
def delete_tareas(id):
    eliminar_tarea = next((tarea for tarea in tareas if tarea['id'] == id), None)

    if eliminar_tarea:
        tareas.remove(eliminar_tarea)
        return jsonify({'mensaje': f'Tarea con id {id} eliminada'}), 200
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    


@app.route ('api/tarea/<int:id>', methods= ['PUT'])
def update_tareas(id): 
    tarea_actualizada = request.json
    tarea = next ((tarea for tarea in tareas if tarea['id']== id), None)

    if tarea: 
        tarea.update(tarea_actualizada)
        return jsonify(tarea), 200 

    else: 
        return jsonify ({'error': 'Tarea no encontrada'}), 404   

if __name__ == '__main__':
    app.run(debug=True)

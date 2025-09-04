from config import app, db
from flasgger import Swagger
from controller import tarefas

app.register_blueprint(tarefas)
swagger = Swagger(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    
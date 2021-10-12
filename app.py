from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ice_db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/edit')
def home1():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route('/')
def list1():
    todo_list = Todo.query.all()
    return render_template("list.html", todo_list=todo_list)


@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("title")
    newTodo = Todo(title=title, complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("home1"))


@app.route('/update/<int:todoId>')
def update(todoId):
    todo = Todo.query.filter_by(id=todoId).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home1"))


@app.route('/delete/<int:todoId>')
def delete(todoId):
    todo = Todo.query.filter_by(id=todoId)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home1"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

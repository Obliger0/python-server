from flask import Blueprint, render_template, request, redirect
from .db import get_all_todos, add_todo, delete_todo_by_id

main = Blueprint('main', __name__)

@main.route('/')
def index():
    todos = get_all_todos()
    return render_template('index.html', todos=todos)

@main.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    add_todo(content)
    return redirect('/')

@main.route('/delete/<int:id>')
def delete(id):
    delete_todo_by_id(id)
    return redirect('/')

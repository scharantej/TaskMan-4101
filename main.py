
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    todos = ['Task 1', 'Task 2', 'Task 3']
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo = request.form['todo']
    todos.append(todo)
    return redirect(url_for('index'))

@app.route('/remove_completed', methods=['POST'])
def remove_completed():
    todos[:] = [todo for todo in todos if not request.form.get(todo, False)]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()

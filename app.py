from flask import Flask, request, redirect, url_for, render_template
import random

app = Flask(__name__)

todos = [
    {
        'id': 1,
        'name': 'Write SQL',
        'checked': False
    },
    {
        'id': 2,
        'name': 'Write Python',
        'checked': True
    }
]

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():

    if(request.method == 'POST'):
        task_name = request.form['task_name']
        cur_id = random.randint(1, 1000)

        if not task_name.strip():
            return redirect('/')

        else:
            todos.append({
                'id': cur_id,
                'name': task_name,
                'checked': False
            })
            return redirect(url_for('home'))

    return render_template('index.html', tasks=todos)

@app.route('/checked/<int:task_id>', methods=['POST'])
def check(task_id):
    for task in todos:
        if task['id'] == task_id:
            task['checked'] = not task['checked']
            break
    
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    global todos
    for task in todos:
        if task['id'] == task_id:
            todos.remove(task)
    return redirect(url_for('home'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit(task_id):

    global todos
    new_task_name = request.form['edit-task']

    if not new_task_name.strip():
            return redirect(url_for('home'))

    for task in todos:
        if task['id'] == task_id:
            task['name'] = new_task_name

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
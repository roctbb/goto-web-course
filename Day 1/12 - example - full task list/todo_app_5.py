from flask import Flask, render_template, redirect, abort, request

tasks = [
    {
        "name": "Пресс качат",
        "description": "3 падхода 20 раз",
        "is_done": True
    },
    {
        "name": "Бегит",
        "description": "3 камэ",
        "is_done": False
    },
    {
        "name": "Турник",
        "description": "5 патходав 10 раз",
        "is_done": True
    },
    {
        "name": "Анжуманя",
        "description": "По ощущеня",
        "is_done": False
    },
    {
        "name": "Гантели",
        "description": "Бицеп, трицеп, плеча",
        "is_done": False
    },
]

app = Flask(__name__)


@app.route('/')
def index():
    done_count = len([task for task in tasks if task['is_done']])
    count = len(tasks)
    return render_template("tasks.html", tasks=tasks, done_count=done_count, count=count)


@app.route('/tasks/<int:id>/done')
def make_done(id):
    if id < 0 or id >= len(tasks):
        abort(404)

    tasks[id]["is_done"] = True

    return redirect('/')


@app.route('/tasks/<int:id>/undone')
def make_undone(id):
    if id < 0 or id >= len(tasks):
        abort(404)

    tasks[id]["is_done"] = False

    return redirect('/')


@app.route('/tasks/<int:id>/delete')
def delete_task(id):
    if id < 0 or id >= len(tasks):
        abort(404)

    del tasks[id]

    return redirect('/')


@app.route('/tasks/add', methods=['post'])
def add_task():
    task_name = request.form.get('task_name')
    task_description = request.form.get('task_description', '')

    if task_name:
        tasks.append({
            "name": task_name,
            "is_done": False,
            "description": task_description
        })

    return redirect('/')


@app.route('/tasks/<int:id>/edit')
def edit_task_page(id):
    if id < 0 or id >= len(tasks):
        abort(404)

    return render_template('edit.html', task=tasks[id], task_id=id)


@app.route('/tasks/<int:id>/edit', methods=['post'])
def edit_task(id):
    if id < 0 or id >= len(tasks):
        abort(404)

    task_name = request.form.get('task_name')
    task_description = request.form.get('task_description', '')

    if task_name:
        tasks[id]['name'] = task_name
        tasks[id]['description'] = task_description

    return redirect('/')


app.run(debug=True)

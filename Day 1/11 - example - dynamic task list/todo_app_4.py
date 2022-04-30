from flask import Flask, render_template, redirect, abort, request

tasks = [
    {
        "name": "Пресс качат",
        "is_done": True
    },
    {
        "name": "Бегит",
        "is_done": False
    },
    {
        "name": "Турник",
        "is_done": True
    },
    {
        "name": "Анжуманя",
        "is_done": False
    },
    {
        "name": "Гантели",
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

@app.route('/tasks/add', methods=['post'])
def add_task():
    task_name = request.form.get('task_name')

    if task_name:
        tasks.append({
            "name": task_name,
            "is_done": False
        })

    return redirect('/')

app.run(debug=True)

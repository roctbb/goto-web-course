from flask import Flask, render_template, redirect, abort

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

# Эта страница показывает список задач
@app.route('/')
def index():
    # Чтобы показать прогресс бар с кол-вом выполненых задач, передадим в шаблон, сколько сделано и сколько их всего
    done_count = len([task for task in tasks if task['is_done']])
    count = len(tasks)
    return render_template("tasks.html", tasks=tasks, done_count=done_count, count=count)


# Чтобы пометить, что задача выполена, сделаем страницу /tasks/НОМЕРЗАДАЧИ/done
@app.route('/tasks/<int:id>/done')
def make_done(id):
    if id < 0 or id >= len(tasks):
        abort(404)

    tasks[id]["is_done"] = True

    # Поскольку у нас уже есть страница с отображением списка задач, можем просто перенаправить туда пользователя
    return redirect('/')

# Эта страница наоборот отмечачет задачу невыполенной
@app.route('/tasks/<int:id>/undone')
def make_undone(id):
    if id < 0 or id >= len(tasks):
        abort(404)

    tasks[id]["is_done"] = False

    return redirect('/')


app.run(debug=True)

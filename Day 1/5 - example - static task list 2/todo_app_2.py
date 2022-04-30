from flask import Flask, render_template

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
    return render_template("tasks.html", tasks=tasks)


app.run(debug=True)

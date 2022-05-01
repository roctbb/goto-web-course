from flask import Flask, render_template

tasks = [
    "Пресс качат",
    "Бегит",
    "Турник",
    "Анжуманя",
    "Гантели"
]

app = Flask(__name__)

@app.route('/')
def index():
    # В шаблон можно передавать не только строки и числа, но и список целиком
    return render_template("tasks.html", tasks=tasks)

app.run(debug=True)
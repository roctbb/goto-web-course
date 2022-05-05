from flask import Flask, render_template

app = Flask(__name__)

@app.route('/example/<int:id>')
def example_page(id):
    return render_template(f"example_{id}.html")

app.run(debug=True)
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

messages = [
    {"author": "test", "text": "welcome"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/messages')
def get_messages():
    num = int(request.args.get('from', 0))

    return jsonify(messages[num:])


@app.route('/api/messages', methods=['POST'])
def send_message():
    author = request.form.get("author", "")
    text = request.form.get("text", "")

    print(request.form)

    if author and text:
        messages.append({"author": author, "text": text})

    return "ok"

app.run(host="0.0.0.0", port=5000, debug=True)
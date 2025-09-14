from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    """Render main chat UI"""
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    """Process user message and return chat output"""
    data = request.json
    user = data.get('user')
    message = data.get('message')
    response = process_message(user, message)
    return jsonify({'response': response})

def process_message(user, message):
    """Dummy message processor"""
    return f'{user}: {message}'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from source.backend.agents.routing.config import INTENTS
from source.backend.agents.routing.graph import ci_graph
from source.backend.agents.sql.graph import sql_graph
from source.backend.utils.langgraph_utils import _print_event
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

    print("\n\nReceived a message with data:", request.json)
    response = process_message(user, message)
    return jsonify({'response': response})

def process_message(user, message):
    """Dummy message processor"""
    state = {
        "messages": [("user", message)],
        "intent_configs": INTENTS
    }

    print("\nProcessing message for user:", user, "\n")
    events = ci_graph.invoke(state, config={"configurable": {"thread_id": str(user)}})
    ai_message = _print_event(events)

    print("\nDone processing message for user:", user)

    return f'{ai_message}'

if __name__ == '__main__':
    app.run(debug=True)

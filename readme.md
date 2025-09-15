# Agentic Chatbot PoC

A simple agentic chatbot 

## Project Structure

```
source/
	ui/
		app.py                # Flask app for web UI
		templates/
			index.html          # Web chat interface
	backend/
		cli_chat.py           # CLI interface
		agents/
			routing/
				config.py         # Intent definitions
				graph.py          # Routing graph logic
			__init__.py
		utils/
			langgraph_utils.py  # Utility functions for LangGraph
run.sh                    # Script to launch web app with Gunicorn
requirements.txt
readme.md
```

## Quickstart

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Web UI
Set Env variable for LLM (Directory: `source/backend/llm/models.py`)
```
os.environ["OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_API_KEY"] = ""
```
based on your deployments specifications

```
chmod +x ./source/run.sh
./source/run.sh
```

Visit [http://localhost:8000](http://localhost:8000) in your browser.

### 3. Run the CLI

```
export PYTHONPATH=$PWD
python source/backend/cli_chat.py
```

## Configuration

- **Intents**: Define and customize in `source/backend/agents/routing/config.py`.
- **Routing Graph**: Modify or extend in `source/backend/agents/routing/graph.py`.

## Requirements

- Python 3.8+
- Flask
- Gunicorn
- langgraph

---

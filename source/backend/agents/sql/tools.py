import json
from langchain_core.runnables import Runnable
from langchain_core.messages import AIMessage
from typing import Literal
from source.backend.agents.routing.state import RoutingState as State

def execute_code(state: State) -> dict:
    """Execute the code."""

    print("\nExecuting code...", state)
    # DUMMY CODE TO EXECUTE
    try:
        generator_result =state["messages"][-1].content
        query = str(generator_result.split(":", maxsplit=1)[-1])
        print(f"\nRunning SQL Query: {query}")
        result = run_sql(query)
    except Exception as e:
        print(f"Error executing code: {e}")
        return {"messages": AIMessage(content=f"Error executing code: {e}")}
    
    print(f"Code executed successfully.\n")
    return {"messages": AIMessage(content="Code executed successfully."), "query_result": result, "sql_query": query}


def run_sql(query):
    return "Code executed successfully"
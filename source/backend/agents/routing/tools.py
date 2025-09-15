import traceback
from langchain_core.runnables import Runnable
from langchain_core.tools import tool
from typing import Literal
from source.backend.agents.routing.state import RoutingState as State
from source.backend.agents.sql.graph import sql_graph

def intialize_chat(state: State) -> dict:
    """Initialize the chat."""
    pass


@tool
def start_intent(
        state: State,
        intent: Literal["troubleshoot", "query_database"],
        start_time: int,
        end_time: int,
        user_friendly_response: str
    ) -> str:
    """
    Tool to start executing an intent
    Args:
        intent (str): The intent to start.
        start_time (int): Start time timestamp in seconds.
        end_time (int): End time timestamp in seconds.
        user_friendly_response (str): A user friendly response for user.
    """
    print("Starting intent:", intent, "from", start_time, "to", end_time)
    print("User friendly response:", user_friendly_response)

    if intent == "query_database":
        try:
            sql_events = sql_graph.invoke(state)
        except Exception as e:
            traceback.print_exc()
            print(f"Error executing intent: {e}")
            return f"Error executing intent: {e}"

        print("\nSQL Events:", sql_events, "\n")
    return "Intent executed successfully."

routing_assistant_tools = [start_intent]

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import tools_condition
from source.backend.agents.routing.state import RoutingState as State
from source.backend.agents.routing.assistant import router_runnable
from source.backend.utils.langgraph_utils import create_tool_node_with_fallback
from source.backend.agents.routing.tools import routing_assistant_tools
from source.backend.agents.routing.assistant import Assistant


def route_tools(state: State):
    next_node = tools_condition(state)
    if next_node == END:
        return END

    ai_message = state["messages"][-1]
    first_tool_call = ai_message.tool_calls[0]
    if first_tool_call["name"] in ['start_intent']:
        return "routing_tools"
    return END


workflow = StateGraph(State)

workflow.add_node("routing_assistant", Assistant(router_runnable))
workflow.add_node("routing_tools", create_tool_node_with_fallback(routing_assistant_tools))

workflow.add_edge(START, "routing_assistant")
workflow.add_conditional_edges(
    "routing_assistant",
    route_tools,
    ["routing_tools", END]
)
workflow.add_edge("routing_tools", "routing_assistant")

memory = InMemorySaver()
ci_graph = workflow.compile(checkpointer=memory)

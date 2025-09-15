from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import tools_condition
from source.backend.agents.sql.state import SQLState as State
from source.backend.agents.sql.assistant import Assistant, planner_runnable, generator_runnable
from source.backend.agents.sql.tools import execute_code


def route_execute(state: State):
    next_node = tools_condition(state)
    if next_node == END:
        return END

    execute_message = state["messages"][-1]
    if "error" in execute_message.content.lower():
        return "generator"
    return END


workflow = StateGraph(State)

workflow.add_node("planner", Assistant(planner_runnable, name="planner"))
workflow.add_node("generator", Assistant(generator_runnable, name="generator"))
workflow.add_node("execute", execute_code)

workflow.add_edge(START, "planner")
workflow.add_edge("planner", "generator")
workflow.add_edge("generator", "execute")
workflow.add_conditional_edges(
    "execute",
    route_execute,
    ["generator", END]
)

memory = InMemorySaver()
sql_graph = workflow.compile(checkpointer=memory)

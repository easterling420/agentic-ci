from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.messages import AIMessage
from source.backend.agents.sql.state import SQLState as State
from source.backend.agents.sql.prompt import PLANNER, GENERATOR
from source.backend.llm.models import llm
from typing_extensions import TypedDict


class PlannerOutput(TypedDict):
    tables: list
    joins: list
    filters: list
    aggregations: list


class GeneratorOutput(TypedDict):
    sql_query: str
    query_explanation: str


class Assistant:
    def __init__(self, runnable: Runnable, name=None):
        self.name = name
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        while True:
            state = {**state}
            result = self.runnable.invoke(state, config)

            if not isinstance(result, dict):
                messages = state["messages"] + [("user", "Respond with correct format output.")]
                state = {**state, "messages": messages}
            else:
                break
        
        print("\nResponse from ", self.name, ": ", result)
        ai_message = AIMessage(content=f"Output from {self.name}: {result}")
        node_key = f"{self.name}_output"

        return {
            "messages": [ai_message],
            node_key: result
        }


planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            PLANNER
        ),  
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

generator_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            GENERATOR
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)


planner_runnable = planner_prompt | llm.with_structured_output(PlannerOutput)
generator_runnable = generator_prompt | llm.with_structured_output(GeneratorOutput)



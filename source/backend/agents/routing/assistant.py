from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig
from source.backend.agents.routing.state import RoutingState as State
from source.backend.agents.routing.prompt import ROUTER_PROMPT
from source.backend.llm.models import llm
from source.backend.agents.routing.tools import routing_assistant_tools


class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        while True:
            state = {**state}
            result = self.runnable.invoke(state)

            if not result.tool_calls and (
                not result.content
                or isinstance(result.content, list)
                and not result.content[0].get("text")
            ):
                messages = state["messages"] + [("user", "Respond with a real output.")]
                state = {**state, "messages": messages}
            else:
                break

        return {"messages": result}


router_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            ROUTER_PROMPT
        ),
        ("placeholder", "{messages}"),
    ]
).partial(time=datetime.now)

router_runnable = router_prompt | llm.bind_tools(routing_assistant_tools)

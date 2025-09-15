from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import AnyMessage, add_messages


class RoutingState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    intent_configs: dict

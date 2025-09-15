from typing import Annotated, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import AnyMessage, add_messages


class SQLState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    sql_query: Optional[str] = None
    query_result: Optional[str] = None

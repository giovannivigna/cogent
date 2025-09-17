from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages


class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

import os
from dotenv import load_dotenv
import sys
from langchain.chat_models import init_chat_model

# Load .env file
load_dotenv()

# Check if OPENAI_API_KEY is set
if not os.getenv("OPENAI_API_KEY"):
    print("Error: OPENAI_API_KEY environment variable is not set.")
    print("Please set your OpenAI API key as an environment variable:")
    print("export OPENAI_API_KEY='your-api-key-here'")
    sys.exit(1)

llm = init_chat_model("openai:gpt-4.1")
import os
from langchain_openai import ChatOpenAI, AzureChatOpenAI
from langchain_anthropic import ChatAnthropic

os.environ["OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_API_KEY"] = ""

openai = ChatOpenAI(
    model="gpt-4o",
    max_tokens=1500,
    timeout=20,
    max_retries=2
)

azure_openai = AzureChatOpenAI(
    azure_endpoint="https://mist-prod.openai.azure.com/",
    api_version="2024-12-01-preview",
    azure_deployment="stage1-gpt4o",
    max_retries=2,
    timeout=20
)


model = ChatAnthropic(model='')

llm = azure_openai

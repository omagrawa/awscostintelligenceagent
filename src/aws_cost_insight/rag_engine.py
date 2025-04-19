import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def ask_question(question: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set in environment.")
    
    chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    response = chat([HumanMessage(content=question)])
    return response.content

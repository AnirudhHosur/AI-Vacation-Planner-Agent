import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import search_tool, wiki_tool, save_tool

# Load env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Missing GOOGLE_API_KEY in .env file")

# Gemini Pro
llm_gemini = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro", temperature=0, google_api_key=api_key
)

# Test
test_prompt = "Who are you?"
response = llm_gemini.invoke(test_prompt)
print(">>> Gemini Test Response:", response.content)
print("=" * 60)

# Simplified response schema
class Response(BaseModel):
    country: str
    cities: list[str]
    duration_days: int
    budget_cad: float
    itinerary: list[str]
    activities: list[str]

parser = PydanticOutputParser(pydantic_object=Response)

# Agent prompt with tool placeholders
prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a vacation planner agent. Use tools if needed, then respond in the following JSON format:

{{
  "country": string,
  "cities": [string],
  "duration_days": int,
  "budget_cad": float,
  "itinerary": [string],
  "activities": [string]
}}

Only output JSON. No explanations.
"""),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
])

# Tool setup
tools = [search_tool, wiki_tool, save_tool]

agent = create_tool_calling_agent(
    llm=llm_gemini,
    prompt=prompt,
    tools=tools,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)

# Run it
query = input("Enter your vacation planning query: ")
raw_response = agent_executor.invoke({"query": query})

# Parse & show
try:
    parsed_response = parser.parse(raw_response.get("output", ""))
    print("Structured Response:", parsed_response)
except Exception as e:
    print("Error parsing response:", e)
    print("Raw Output:", raw_response.get("output", ""))

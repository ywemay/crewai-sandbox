from dotenv import load_dotenv
from langchain_community.llms import Ollama
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter

from crewai import Agent, Task, Crew, Process

from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor

from langchain.sql_database import SQLDatabase

# import psycopg2 # pip install psycopg-binary
import os

load_dotenv()

print(os.getenv('POSTGRES_URI'))
print(os.getenv('OLLAMA_BASE_URL'))

# db = SQLDatabase.from_uri('postgresql+psycopg2://admin:password123@localhost/admin')
# print(db)

# https://api.python.langchain.com/en/latest/llms/langchain_community.llms.ollama.Ollama.html
ollama_mistral = Ollama(base_url=os.getenv('OLLAMA_BASE_URL'), model="mistral")


researcher = Agent(
  role='Researcher',
  goal='Research new AI insights',
  backstory='You are an AI research assistant.',
  verbose=True,
  # tools=[search_tool],
  allow_delegation=False,
  llm=ollama_mistral
  # llm=openai_llm
)

writer = Agent(
  role='Writer',
  goal='Write compelling and engaging blog posts about AI trends',
  backstory='You are an AI blog post writer who specializes in writing stories about technology',
  verbose=True,
  allow_delegation=False,
  llm=ollama_mistral
  # llm=openai_llm
)

task1 = Task(description='Investigate the latest AI trends', agent=researcher)
task2 = Task(description='Write a compelling blog post based on latest AI trends', agent=writer)

crew = Crew (
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2,
  process=Process.sequential
)

result = crew.kickoff()

print(result)
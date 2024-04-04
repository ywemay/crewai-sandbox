from langchain_community.llms import Ollama
# import openai
from crewai import Agent, Task, Crew, Process
# import requests

import os

# os.environ["OPENAI_API_BASE"]='http://192.168.0.90:11434/v1'
# os.environ["OPENAI_MODEL_NAME"]='mistral'
# os.environ["OPENAI_API_KEY"]=''

from langchain_community.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()


# os.environ["OPENAI_API_KEY"] = "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"
# openai.api_key = "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"

# ollama_host = "http://192.168.0.90:11434"
ollama_mistral = Ollama(model="mistral")
#
# from langchain_openai import ChatOpenAI
# openai_llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7)

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
  process=Process.sequential,
  share_crew=False
)

result = crew.kickoff()

print(result)
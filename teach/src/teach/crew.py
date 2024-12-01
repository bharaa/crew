from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from teach.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

import os
from crewai import Agent, LLM
# from crewai_tools import PDFSearchTool
from langchain_openai import ChatOpenAI
from teach.tools.custom_tool import serperTool 
from teach.tools.arduino import CompileAndUploadToArduinoTool

llm = ChatOpenAI(
	model="ollama/llama3.1:latest",
	base_url="http://localhost:11434/v1",
	)

tool = CompileAndUploadToArduinoTool(
    ino_file_dir="./tmp",
    board_fqbn="arduino:avr:uno",
    port="/dev/ttyUSB0"
)

# get api key from .env file
GROQ_API_KEY=os.getenv('GROQ_API_KEY')
os.environ["OPENAI_API_KEY"] = "sk-proj-1111"

# pdf_tool = PDFSearchTool(pdf="/home/vision/tool/teach/src/teach/TQM.pdf",)

# make custom llm
# llm= LLM(
#     model="groq/Llama3-8b-8192",
#     base_url="https://api.groq.com/openai/v1",
#     api_key=GROQ_API_KEY
# )

@CrewBase
class TeachCrew():
	"""Teach crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			llm=llm,
			verbose=True,
			allow_delegation=False,
			#tools=[serperTool()], # Example of custom tool, loaded on the beginning of file
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			llm=llm,
			verbose=True,
			allow_delegation=False,
			tools=[tool],
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			output_file="tmp/tmp.ino",
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Teach crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			memory=False,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("MODEL")
BASE_URL = os.getenv("BASE_URL")
MAX_TOKENS = os.getenv("MAX_TOKENS")
MAX_RPM = os.getenv("MAX_RPM")
TEMPERATURE = os.getenv("TEMPERATURE")

llm = LLM(
    model=MODEL,
    base_url=BASE_URL,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS
)

@CrewBase
class PracticesProblemsAgent():
	"""PracticesProblemsAgent crew"""
	agents_config = 'config/problemsolver.yaml'
	tasks_config = 'config/practice_problems_task.yaml'

	@agent
	def problemsolver(self) -> Agent:
		return Agent(
            config=self.agents_config['problemsolver'],
            llm = llm,
            verbose=True
        )

	@task
	def practice_problems_task(self) -> Task:
		return Task(
			config=self.tasks_config['practice_problems_task'],
			output_file="temp/practice_problems.md",
		)
    
	@crew
	def practice_problems_crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
            max_rpm=MAX_RPM
        )

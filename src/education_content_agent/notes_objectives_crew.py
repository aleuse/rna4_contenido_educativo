from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("MODEL")
BASE_URL = os.getenv("BASE_URL")

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
class NotesObjectivesAgent():
	"""NotesObjectivesAgent crew"""
	agents_config = 'config/scholar.yaml'
	tasks_config = 'config/notes_objectives_task.yaml'

	@agent
	def scholar(self) -> Agent:
		return Agent(
			config=self.agents_config['scholar'],
            llm = llm,
			verbose=True
		)

	@task
	def class_notes_task(self) -> Task:
		return Task(
			config=self.tasks_config['class_notes_task'],
            output_file="temp/class_notes.md",
			async_execution=True
		)

	@task
	def learning_objectives_task(self) -> Task:
		return Task(
			config=self.tasks_config['learning_objectives_task'],
            output_file="temp/learning_objectives.md",
		)
    
	@crew
	def notes_objectives_crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
            max_rpm=MAX_RPM
        )

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
class DiscussQuestionsAgent():
	"""DiscussQuestionsAgent crew"""
	agents_config = 'config/debater.yaml'
	tasks_config = 'config/discussion_questions_task.yaml'

	@agent
	def debater(self) -> Agent:
		return Agent(
			config=self.agents_config['debater'],
			llm = llm,
			verbose=True
		)

	@task
	def discussion_questions_task(self) -> Task:
		return Task(
			config=self.tasks_config['discussion_questions_task'],
			output_file="temp/discussion_questions.md",
		)
    
	@crew
	def discussion_questions_crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
            max_rpm=MAX_RPM
        )

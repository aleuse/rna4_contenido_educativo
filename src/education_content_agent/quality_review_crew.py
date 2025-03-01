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
class QualityReviewAgent():
	"""DiscussQuestionsAgent crew"""
	agents_config = 'config/reviewer.yaml'
	tasks_config = 'config/quality_review_task.yaml'

	@agent
	def reviewer(self) -> Agent:
		return Agent(
			config=self.agents_config['reviewer'],
			llm = llm,
			verbose=True
		)

	@task
	def quality_review_task(self) -> Task:
		return Task(
			config=self.tasks_config['quality_review_task'],
            # human_input=True,
			output_file="final_report.md",
		)
    
	@crew
	def quality_review_crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
            max_rpm=MAX_RPM
        )


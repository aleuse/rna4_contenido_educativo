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
class TeachingStyleAgent():
	"""DiscussQuestionsAgent crew"""
	agents_config = 'config/analyzer.yaml'
	tasks_config = 'config/teaching_style_analysis_task.yaml'

	@agent
	def analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['analyzer'],
			llm = llm,
			verbose=True
		)

	@task
	def teaching_style_analysis_task (self) -> Task:
		return Task(
			config=self.tasks_config['teaching_style_analysis_task'],
			output_file="temp/teaching_style_analysis.md",
		)
    
	@crew
	def teaching_style_analysis_crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
            max_rpm=MAX_RPM
        )


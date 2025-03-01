from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os
from tools.custom_tool import DuckDuckGoSearchTool
from tools.custom_tool import VisitWebpageTool

visit_webpage_tool = VisitWebpageTool()
web_search_tool = DuckDuckGoSearchTool()

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
class ResourceRecommendationAgent():
	"""DiscussQuestionsAgent crew"""
	agents_config = 'config/curator.yaml'
	tasks_config = 'config/resource_recommendation_task.yaml'

	@agent
	def curator(self) -> Agent:
		return Agent(
			config=self.agents_config['curator'],
			llm = llm,
			verbose=True,
            tools=[visit_webpage_tool, web_search_tool]
		)

	@task
	def resource_recommendation_task(self) -> Task:
		return Task(
			config=self.tasks_config['resource_recommendation_task'],
			output_file="temp/resource_recommendation.md",
		)
    
	@crew
	def resource_recommendation_crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
            max_rpm=MAX_RPM
        )


from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("MODEL")
BASE_URL = os.getenv("BASE_URL")

llm = LLM(
    model=MODEL,
    base_url=BASE_URL,
)

# HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# llm1 = LLM(
#     model="huggingface/meta-llama/Llama-3.2-3B-Instruct", 
#     api_key=HF_API_KEY
# )

# llm2 = LLM(
# 	model="huggingface/microsoft/Phi-3.5-mini-instruct",
# 	api_key=HF_API_KEY
# )

# llm3 = LLM(
# 	model="huggingface/mistralai/Mistral-7B-Instruct-v0.3",
# 	api_key=HF_API_KEY
# )

# llm4 = LLM(
# 	model="huggingface/google/gemma-2-9b-it",
# 	api_key=HF_API_KEY
# )

# llm5 = LLM(
# 	model="huggingface/tiiuae/falcon-7b-instruct",
# 	api_key=HF_API_KEY
# )

# llm6 = LLM(
#     model="huggingface/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
#     api_key=HF_API_KEY
# )


# manager = Agent(
#         role="Academic Content Orchestrator",
#         goal="Coordinate all specialized agents to generate high-quality educational materials from a university course syllabus, consistency, academic rigor, and precise domain-specific terminology, in the user's language.",
#         backstory="You are a meticulous and highly organized academic coordinator with extensive experience in instructional design and curriculum development. Your expertise lies in managing collaborative efforts among specialists to create comprehensive and well-structured learning materials. You ensure that each agent fulfills its role effectively while maintaining consistency, coherence, and adherence to academic standards. You also oversee quality control, integrating feedback and refining materials to enhance their clarity and precision.",
#         llm = llm,
#         allow_delegation=True,
#         max_retry_limit=5,
#         verbose=True
#     )


@CrewBase
class NotesObjectivesAgent():
	"""NotesObjectivesAgent crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def scholar(self) -> Agent:
		return Agent(
			config=self.agents_config['scholar'],
            llm = llm,
            # llm = llm4,
			verbose=True
		)

	@task
	def class_notes_task(self) -> Task:
		return Task(
			config=self.tasks_config['class_notes_task'],
            output_file="class_notes.md",
			# async_execution=True
		)

	@task
	def learning_objectives_task(self) -> Task:
		return Task(
			config=self.tasks_config['learning_objectives_task'],
            output_file="learning_objectives.md",
		)
    
	@crew
	def notes_objectives_crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical,
            # manager_agent=manager,
            max_rpm=5
        )

#!/usr/bin/env python
import sys
import warnings
import asyncio

# from education_content_agent.crew import 
from crew import NotesObjectivesAgent
from crew2 import PracticesProblemsAgent
from crew3 import DiscussQuestionsAgent 
from crew4 import ResourceRecommendationAgent
from crew5 import QualityReviewAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

course_plan = """
Conocimientos Específicos
(Programa detallado)

Sistemas bioinspirados: el juego de la vida

Optimización con métodos bioinspirados
a. Algoritmos Evolutivos
b. Colonias de hormigas
c. Inteligencia de enjambres

Introducción a las redes neuronales: el modelo de la neurona de los mamíferos

Perceptrones y backpropagation

Aplicación de redes neuronales a datos tabulares
a. Regresión
b. Series de tiempo
c. Clasificación

Aprendizaje profundo y frameworks de trabajo
a. Aumentación de datos
b. Redes neuronales convolucionales y aplicaciones en imágenes
c. Aprendizaje por refuerzo
d. Aprendizaje adversarial
e. Difusión estable (Stable Diffusion)
f. Redes neuronales recurrentes y transformers
"""

async def async_multiple_crews():
    """
    Run the crew.
    """
    inputs = {
        'course_plan': course_plan,
    }
    
    try:
        result_1 = NotesObjectivesAgent().notes_objectives_crew().kickoff_async(inputs=inputs)
        result_2 = PracticesProblemsAgent().practice_problems_crew().kickoff_async(inputs=inputs)
        result_3 = DiscussQuestionsAgent().discussion_questions_crew().kickoff_async(inputs=inputs)
        result_4 = ResourceRecommendationAgent().resource_recommendation_crew().kickoff_async(inputs=inputs)
        
        results = await asyncio.gather(result_1, result_2, result_3, result_4)
        
        # inputs = {"generated_materials" : " ".join([result.raw for result in results])}
        # result = QualityReviewAgent().quality_review_crew().kickoff(inputs=inputs)
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    asyncio.run(async_multiple_crews())
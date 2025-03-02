#!/usr/bin/env python
import sys
import os
import warnings
import asyncio

from notes_objectives_crew import NotesObjectivesAgent
from practice_problems_crew import PracticesProblemsAgent
from discussion_questions_crew import DiscussQuestionsAgent 
from resource_recommendation_crew import ResourceRecommendationAgent
# from quality_review_crew import QualityReviewAgent
from teaching_style_analysis_crew import TeachingStyleAgent
from extract_info import DocumentExtractor

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Crear una instancia del extractor
extractor = DocumentExtractor(idioma='es')

RUTA_INPUT = "Docs"

def extract_text(ruta):
    """
    Extrae texto de un archivo TXT, DOCX o PDF.
    """
    try:
        texto = extractor.procesar_carpeta(ruta)
    except Exception as e:
        raise Exception(f"Error al extraer texto de {ruta}: {e}")
    
    return texto

def read_results():
    with open("temp/class_notes.md", "r", encoding='utf-8') as file:
        class_notes = file.read()
    with open("temp/learning_objectives.md", "r", encoding='utf-8') as file:
        learning_objectives = file.read()
    with open("temp/discussion_questions.md", "r", encoding='utf-8') as file:
        discussion_questions = file.read()
    with open("temp/resource_recommendation.md", "r", encoding='utf-8') as file:
        resource_recommendations = file.read()
    
    results = "\n"
    results += "# Class Notes\n"
    results += class_notes + "\n"
    results += "# Learning Objectives\n"
    results += learning_objectives + "\n"
    results += "# Discussion Questions\n"
    results += discussion_questions + "\n"
    results += "# Resource Recommendations\n"
    results += resource_recommendations + "\n"
    return results
    


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

def run_teaching_style_analysis(course_plan):
    inputs = {
        'course_plan': course_plan,
    }
    
    try:
        result = TeachingStyleAgent().teaching_style_analysis_crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
    return result.raw

async def async_multiple_crews(course_plan, teaching_style_analysis):
    """
    Run the crew.
    """
    inputs = {
        'course_plan': course_plan,
        'teaching_style_analysis': teaching_style_analysis,
    }
    
    try:
        result_1 = NotesObjectivesAgent().notes_objectives_crew().kickoff_async(inputs=inputs)
        result_2 = PracticesProblemsAgent().practice_problems_crew().kickoff_async(inputs=inputs)
        result_3 = DiscussQuestionsAgent().discussion_questions_crew().kickoff_async(inputs=inputs)
        result_4 = ResourceRecommendationAgent().resource_recommendation_crew().kickoff_async(inputs=inputs)
        
        results = await asyncio.gather(result_1, result_2, result_3, result_4)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    
# def run():
#     results = read_results()
#     print(f"Results: {results}")
#     inputs = {"generated_materials" : results}
#     QualityReviewAgent().quality_review_crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    course_syllabus = extract_text(RUTA_INPUT)
    teaching_style_analysis = run_teaching_style_analysis(course_syllabus)
    asyncio.run(async_multiple_crews(course_syllabus, teaching_style_analysis))
    # run()
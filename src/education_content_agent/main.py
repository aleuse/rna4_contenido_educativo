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
from md2pdf import DocumentConverter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Crear una instancia del extractor
extractor = DocumentExtractor(idioma='es')

# Crear una instancia del conversor
converter = DocumentConverter()

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

def convert_results():
    """
    Convierte el contenido Markdown a PDF.
    """
    try:
        # Generar el PDF
        converter.markdown_to_pdf("education_materials.pdf")
    except Exception as e:
        raise Exception(f"Error al convertir a PDF: {e}")
    

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
    convert_results()
    # run()
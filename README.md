# 📚 Agente Inteligente para Generación de Contenido Educativo

---

## 🎯 **Objetivo del Proyecto**

Desarrollar un **agente inteligente** que asista en la **creación de contenido educativo**, automatizando la generación de materiales didácticos para mejorar la enseñanza y el aprendizaje.

## 📌 **Objetivos Específicos**

El agente deberá ser capaz de:

- **Analizar y comprender** programas de curso en formatos comunes (PDF, TXT, DOCX).
- **Generar materiales educativos**, incluyendo:
  - 📝 **Notas de clase** detalladas para cada tema.
  - 🔢 **Problemas de práctica** con soluciones.
  - ❓ **Preguntas para discusión** en clase.
  - 🎯 **Objetivos de aprendizaje** claros y estructurados.
  - 📖 **Lecturas y recursos sugeridos** para profundización.

---

## 📂 **Estructura del Proyecto**

### 🧠 **Agentes y Tareas**
- **Ubicación:** `src/education_content_agent/config`
- **Descripción:**
  - **Prompts para los agentes**, con:
    - Rol específico.
    - Objetivo principal.
    - Contexto relevante.
  - **Prompts para las tareas**, con:
    - Descripción detallada.
    - Salida esperada.
    - Agente encargado.

### 🛠️ **Herramientas**
- **Ubicación:** `src/education_content_agent/tools`
- **Descripción:** Módulos personalizados para:
  - **Navegar y extraer contenido** de páginas web.
  - **Procesar información** relevante para los materiales educativos.

### 📜 **Scripts Principales**
- **Ubicación:** `src/education_content_agent`
- **Descripción:** Contiene los scripts que gestionan la ejecución de los agentes y sus tareas.

### 📁 **Documentos de Entrada**
- **Ubicación:** `docs`
- **Descripción:** En este carpeta se deben colocar los documentos de entrada.

### 📁 **Temporal**
- **Ubicación:** `temp`
- **Descripción:** En este carpeta se crean archivos intermedios en la generación del resultado final.

### 📁 **Resultado**
- **Ubicación:** `output`
- **Descripción:** En este carpeta se entrega el resultado final.

### ✅ **Pruebas**
- **Ubicación:** `test`
- **Descripción:** Contiene pruebas realizadas con diferentes modelos de lenguaje (LLMs) para evaluar el desempeño del agente.

---

## ⚙️ **Requisitos del Sistema**

- **Lenguaje:** Python 3.10+
- **Librerías principales:**
  - [`CrewAI`](https://github.com/crewai/crewai) → Gestión de agentes.
  - [`DuckDuckGo-Search`](https://pypi.org/project/duckduckgo-search/) → Búsquedas web.
  - [`Markdownify`](https://pypi.org/project/markdownify/) → Conversión de HTML a Markdown.
- 📌 **Revisar** [`requirements.txt`](requirements.txt) para más detalles.
- **Ollama**: [Descargar e instalar](https://ollama.com/download).

---

## 🚀 **Cómo Ejecutar el Proyecto**

1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/aleuse/rna4_contenido_educativo.git
    cd rna4_contenido_educativo
    ```

2. **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate     # En Windows
    ```

3. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecutar localmente el modelo deseado:**
    ```bash
    ollama run llama3.2
    ```

5. **Configurar los parámetros:**  
   Crear un archivo `.env` en la carpeta raíz y definir las siguientes variables:

    ```ini
    BASE_URL=http://localhost:11434  # URL donde se ejecuta el modelo
    MODEL=ollama/NombreDelModelo
    MAX_TOKENS=...
    MAX_RPM=...
    TEMPERATURE=...
    ```

6. **Colocar los documentos de entrada:**
    En la carpeta `docs` colocar los documentos que se quieren usar como entrada.

7. **Ejecutar el código:**
    ```bash
    python src/education_content_agent/main.py
    ```

---

## 📌 **Notas Adicionales**
- Asegúrate de que **Ollama esté ejecutándose** antes de lanzar el script.
- Se recomienda realizar **pruebas con diferentes modelos** para evaluar cuál ofrece mejores resultados en la generación de contenido.


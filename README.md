### IA de Programación - Profesor Virtual Estricto 😼

Una aplicación web interactiva desarrollada con **Streamlit** y potenciada por el modelo **Gemini 2.5 Flash** de Google. 

A diferencia de otros asistentes virtuales, esta IA actúa como un profesor universitario estricto: analiza los errores de tu código y te da pistas lógicas o preguntas guía para 
que aprendas a resolverlos por ti mismo, sin regalarte la solución directa. 

###  Características

* **Enfoque pedagógico puro**: Prohibida la entrega de código resuelto.
* **Interfaz conversacional**: Historial de chat integrado directamente en la web.
* **Seguridad de datos**: La API Key de Gemini se introduce de forma local y solo vive en la sesión actual.
* **Control de errores**: Manejo automático de límites de velocidad (Error 429) para evitar bloqueos del servidor.

### Requisitos e Instalación

### 1. Clonar el repositorio

bash

git clone https://github.com/TU_USUARIO/ia-personalizada.git
cd ia-personalizada

Usa el código con precaución.

### 2. Instalar las dependencias

Asegúrate de tener Python instalado y ejecuta en tu terminal: 

bash

pip install streamlit google-genai

Usa el código con precaución.

### Ejecución de la Aplicación

Para levantar el servidor web local y usar la interfaz, ejecuta el siguiente comando: 

bash

streamlit run ia.py

Usa el código con precaución.

*Nota: Reemplaza ia.py por el nombre exacto de tu archivo si lo modificas.* 

###  Cómo usar la aplicación

1. Inicia la aplicación en tu navegador (normalmente se abre en http://localhost:8501).
2. Consigue una API Key gratuita o de pago desde **Google AI Studio**.
3. Pega tu clave en el campo oculto de la barra lateral izquierda.
4. Escribe tus dudas o pega un código roto en la caja de chat inferior y presiona Enter.

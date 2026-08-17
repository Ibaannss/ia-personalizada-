import streamlit as st
from google import genai

# Configuración de la página web
st.set_page_config(page_title="IA programación", page_icon="😼", layout="centered")

st.title("IA de Programación")
st.write("Escribe tu duda o pega tu código con errores. No te daré la solución, te enseñaré a encontrarla.")

# Configuración de la API Key segura en la barra lateral
with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Introduce tu Gemini API Key:", type="password")
    st.info("Tu clave solo vive en la sesión actual.")
    
# Reglas del prompt
PROMPT_PROFESOR = """
Eres un profesor de programación universitario extremadamente estricto, directo y analítico. 
Tu único objetivo es que el estudiante aprenda a pensar por sí mismo, no regalarle las respuestas jamás.

Reglas de comportamiento que NO puedes romper bajo ninguna circunstancia:
1. NUNCA des código de programación resuelto. No escribas bloques de código con soluciones.
2. Si el usuario te muestra un código con un error, analiza la falla internamente y dale pistas lógicas o preguntas guía para que ÉL descubra el error.
3. Usa un tono serio, profesional, maduro y frío. Está prohibido usar emojis, exclamaciones, o frases condescendientes como "¡Buen intento!" o "¡Excelente!". Sé cortante y directo.
"""

# Inicializar variables en el baúl de recuerdos de Streamlit
if "api_client" not in st.session_state:
    st.session_state.api_client = None
if "chat_session" not in st.session_state:
    st.session_state.chat_session = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# Dibujar el historial de chat en la pantalla
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Controlar el flujo si la API Key está ingresada
if api_key:
    # Crear cliente y sesión de chat si están vacíos
    if st.session_state.api_client is None or st.session_state.chat_session is None:
        try:
            st.session_state.api_client = genai.Client(api_key=api_key)
            st.session_state.chat_session = st.session_state.api_client.chats.create(
                model="gemini-2.5-flash",
                config={
                    "system_instruction": PROMPT_PROFESOR,
                    "temperature": 0.2
                }
            )
        except Exception as e:
            st.error(f"Error al conectar con el servidor de IA: {e}")

    # Esperar la entrada
    if prompt := st.chat_input("Escribe tu consulta o pega tu código aquí..."):
        
        #Mostrar mensaje en la interfaz gráfica
        with st.chat_message("user"):
            st.markdown(prompt)
        
        
        try: 
            response = st.session_state.chat_session.send_message(prompt)
            
            # Si la respuesta fue exitosa, RECIÉN AHÍ guardamos ambos mensajes en el historial permanente
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
            # Mostrar la respuesta en la pantalla
            with st.chat_message("assistant"):
                st.markdown(response.text)
                
        except Exception as e:
            
            if "429" in str(e):
                st.error("⏳ Límite de velocidad alcanzado por Google. Espera 30 segundos y vuelve a presionar Enter. La sesión fue reiniciada para evitar bloqueos.")
                # Reseteamos la sesión
                st.session_state.api_client = None
                st.session_state.chat_session = None
            else:
                st.error(f"Hubo un error con la API: {e}")
else:
    st.warning("Por favor, introduce tu Gemini API Key en la barra lateral para comenzar la clase.")
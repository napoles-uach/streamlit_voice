import streamlit as st
import streamlit.components.v1 as components

# Crear el componente personalizado
_component_func = components.declare_component("voice", path="")

# Definir la función del componente
def voice(name=None, key=None):
    _COMPONENT_HTML = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Transcripción de Voz</title>
    </head>
    <body>
        <h2>Presiona el botón y habla:</h2>
        <button onclick="startDictation()">Iniciar</button>
        <p id="result"></p>
        <script>
            function startDictation() {
                if (window.hasOwnProperty('webkitSpeechRecognition')) {
                    var recognition = new webkitSpeechRecognition();

                    recognition.continuous = false;
                    recognition.interimResults = false;

                    recognition.lang = "es-ES";
                    recognition.start();

                    recognition.onresult = function(e) {
                        document.getElementById('result').innerHTML = e.results[0][0].transcript;
                        sendToStreamlit(e.results[0][0].transcript);
                        recognition.stop();
                    };

                    recognition.onerror = function(e) {
                        recognition.stop();
                    }
                }
            }

            function sendToStreamlit(text) {
                const data = {
                    text: text
                };
                const streamlitComponent = window.parent.streamlitComponent;
                streamlitComponent.sendMessage(data);
            }
        </script>
    </body>
    </html>
    """
    component_value = _component_func(name=name, key=key, default="", html=_COMPONENT_HTML, height=300)
    return component_value

import streamlit as st
import streamlit.components.v1 as components

# Definir el componente HTML
def voice(name=None, key=None):
    _COMPONENT_HTML = f"""
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
                const streamlitComponent = window.parent.document.querySelector('iframe').contentWindow.streamlit;
                streamlitComponent.setComponentValue(text);
            }
        </script>
    </body>
    </html>
    """
    component_value = components.html(_COMPONENT_HTML, height=300)
    return component_value

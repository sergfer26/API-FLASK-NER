from flask import Flask, request, jsonify, render_template
import spacy
from ner_client import NamedEntityClient

# Carga de modelo NLP de SpaCY
nlp = spacy.load('es_core_news_sm')
client = NamedEntityClient(nlp)

# Creación de instancia de Aplicación de Flask
app = Flask(__name__)

# método `GET` para deplegar API en servidor 
@app.route('/')
def index():
    return render_template('index.html')

# método `POST` para hacer `request` desde el servidor
@app.route('/ner-api-flask', methods=['POST'])
def process():
    # Carga de archivo JSON para backend 
    data = request.json
    # Extracción de información para procesamiento
    sentences = data['oraciones']
    # Procesamiento de información: Identificación de entidades
    result = client.get_entities(sentences)
    # Carga de resultados
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)


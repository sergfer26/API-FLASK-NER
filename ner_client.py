from flask import jsonify

class NamedEntityClient(object):

    def __init__(self, model):
        self.model = model # Instancia de un modelo NLP

    def get_entities(self, sentences):
        '''
        Argumentos
        ----------
        sentences : list
            Lista que contiene cadenas de texto 
        '''
        results = list()
        for sen in sentences:
            doc = self.model(sen)

            entities = [
                # "(San Fransico, LOC)"
                (ent.text, ent.label_ ) for ent in doc.ents
            ]
            results.append({
                "oración": sen, # "San Francisco considera prohibir los robots de entrega en la acera."
                "entidades": dict(entities) # "San Fransico: LOC"
            })
        return {"resultado": results}




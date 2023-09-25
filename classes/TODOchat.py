import random
preguntas= [
    {"pregunta":"Pregunta 1", "respuesta":{
        "tipo a":["respuesta a 1","respuesta a 2"],
        "tipo b":["respuesta b 1","respuesta b 2"],
        "tipo c":["respuesta c 1","respuesta c 2"],
        "tipo d":["respuesta d 1","respuesta d 2"]
    }},
     {"pregunta":"Pregunta 2", "respuesta":{
        "tipo a":["respuesta a 1","respuesta a 2"],
        "tipo b":["respuesta b 1","respuesta b 2"],
        "tipo c":["respuesta c 1","respuesta c 2"],
        "tipo d":["respuesta d 1","respuesta d 2"]
     }},
      {"pregunta":"Pregunta 3", "respuesta":{
        "tipo a":["respuesta a 1","respuesta a 2"],
        "tipo b":["respuesta b 1","respuesta b 2"],
        "tipo c":["respuesta c 1","respuesta c 2"],
        "tipo d":["respuesta d 1","respuesta d 2"]
      }}
    ]
def chat(tipo):
    for x in random.sample(preguntas,3):
        print(x["pregunta"])
        print(x["respuesta"][tipo])


chat("tipo a")
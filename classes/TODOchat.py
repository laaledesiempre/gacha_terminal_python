import random
TYPOS={
    "TIPO_A":"tipo a",
}
INTERACTION_EFFECT={
    "POSITIVE":50,
    "LITTLE_POSITIVE":25,
    "OK": 5,
    "IGNORED":0,
    "DISLIKED":-5,
    "BAD":-25,
    "AWFUL":-50
}
preguntas= [
    {"pregunta":"Pregunta 1", "respuesta":{
        "tipo a":["respuesta a 1 1","respuesta a 2 1"],
        "tipo b":["respuesta b 1 1","respuesta b 2 1"],
        "tipo c":["respuesta c 1 1","respuesta c 2 1"],
        "tipo d":["respuesta d 1 1","respuesta d 2 1"],
        "typos_effect":{
            "tipo a": INTERACTION_EFFECT["BAD"],
            "tipo b": INTERACTION_EFFECT["BAD"],
            "tipo c": INTERACTION_EFFECT["BAD"],
            "tipo d": INTERACTION_EFFECT["BAD"]
            }
        
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
    preguntas_generadas=random.sample(preguntas,3)
    for i,x in enumerate(preguntas_generadas):
        print(f"{i+1}) {x['pregunta']}")
    while True:
        try:
            selected = int(input("Choose one: "))
            print(preguntas_generadas[selected-1]["respuesta"][tipo])
            break
        except:
            print("Non valid option")



chat("tipo b")
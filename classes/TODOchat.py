import random
TYPOS={
    "SHY":"shy",
    "FUNNY":"funny",
    "SERIOUS":"serious",
    "OBEDIENT":"obedient",
    
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
    {"pregunta":"¿Como estas?", "respuesta":{
        TYPOS["SHY"]:["Oh, emm, me encuentro bien, gracias por preguntar","D..De verdad le importa? gracias, me encuentro bien"],
        TYPOS["FUNNY"]:["Bien, pasa algo?","Ja, bien"],
        "serious":["No creo que sea importante","Creo que hay cosas mas importantes ahora"],
        "obedient":["Deberia estar haciendo algo verdad? lo lamento! me pondre a trabajar","Mis sentimientos siempre detras del deber, entendido"],
        "typos_effect":{
            "shy": INTERACTION_EFFECT["OK"],
            "funny": INTERACTION_EFFECT["IGNORED"],
            "serious": INTERACTION_EFFECT["IGNORED"],
            "obedient": INTERACTION_EFFECT["DISLIKE"]
            }
        
    }},
     {"pregunta":"¿Que haces?", "respuesta":{
        "shy":["Oh, ¿me estuvo observando? ","OH me asusto!"],
        "funny":["¿Que le importa? es broma... je","Oh... emmm, algo... creo"],
        "serious":["Trabajando","Lo que usted me pido"],
        "obedient":["Mi deber , como debe ser!","Lo que usted ordene! estoy para servirle!"],
        "typos_effect":{
            "shy": INTERACTION_EFFECT["DISLIKE"],
            "funny": INTERACTION_EFFECT["DISLIKED"],
            "serious": INTERACTION_EFFECT["IGNORED"],
            "obedient": INTERACTION_EFFECT["LITTLE_POSITIVE"]
            }
    }},

      {"pregunta":"¿Puedo ayudarte?", "respuesta":{
        "tipo a":["Yo... yo creo que puedo sola, pero gracias","Oh, de... de verdad haria eso por mi?"],
        "tipo b":["Cree que soy inutil acaso? bha, me vendria bien alguien con quien charlar","See, por que no?"],
        "tipo c":["No","Dejeme trabajar en paz porfavor"],
        "tipo d":["Soy completamente capaz de cada tarea que me ordene! no hace falta su participacion","respuesta d 2"],
        "typos_effect":{
            "shy": INTERACTION_EFFECT["LITTLE_POSITIVE"],
            "funny": INTERACTION_EFFECT["OK"],
            "serious": INTERACTION_EFFECT["BAD"],
            "obedient": INTERACTION_EFFECT["DISLIKE"]
            }
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



chat(TYPOS["SHY"])
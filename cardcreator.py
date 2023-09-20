import random

names= ["Rebeca","Ana","Catalina"]

surname= ["The great", "Magnificent", "Milova", "Parka"]

stats=[
    "STR",
    "INT",
    "AGI",
    "WIS",
    "SPD"
    ]

casual= [1,2,2,2,2]

normal= [2,2,2,3,3]

good= [3,3,2,2,4]

epic= [3,3,4,4,4]

legendary = [3,4,4,5,5]

master = [5,5,5,5,5]

def createCard(level):
    list_of_habilities_multiplier= level.copy()
    random.shuffle(list_of_habilities_multiplier)
    habilities_value= []
    for x in range(5):
        habilities_value.append(int((random.randrange(min(list_of_habilities_multiplier),max(list_of_habilities_multiplier)+1,)/10)*list_of_habilities_multiplier[x]*10))
    return habilities_value
    
print(createCard(casual))
print(createCard(normal))
print(createCard(good))
print(createCard(epic))
print(createCard(legendary))
print(createCard(master))

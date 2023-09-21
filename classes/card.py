import random
from .constants import stats, names, surnames, relationship_states
class Card:
    def __init__(self,level):
            list_of_habilities_multiplier= level.copy()
            random.shuffle(list_of_habilities_multiplier)
            habilities_value= []
            for x in range(5):
                habilities_value.append(int((random.randrange(min(list_of_habilities_multiplier),max(list_of_habilities_multiplier)+1,)/10)*list_of_habilities_multiplier[x]*10))
            habilities={}
            for i,x in enumerate(stats):
                habilities[x]=habilities_value[i]
                
            self.habilities = habilities
            self.Blood = int(min(habilities_value)*random.random()+sum(level))
            self.name = random.choice(names)+ " " +random.choice(surnames)
            self.friendship = 0
            self.love = 0
            self.relationship = relationship_states["SOLDIER"]
    def show(self):
            return f"""
name: {self.name}
Blood: {self.Blood}

    STR: {self.habilities["STR"]}
    INT: {self.habilities["INT"]}
    AGI: {self.habilities["AGI"]}
    WIS: {self.habilities["WIS"]}
    SPD: {self.habilities["SPD"]}
            """
    def chat(self):
          print("you just chatted")
          self.friendship = self.friendship+1
          print(f"Your friendshipp is now {self.friendship}")
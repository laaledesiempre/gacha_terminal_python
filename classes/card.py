import random
from .constants import stats, names, surnames, relationship_states, age_range, relationship_adder

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

            self.age = random.randrange(age_range[0],age_range[1])

            self.friendship = 0

            self.love = 0

            self.relationship = relationship_states["SOLDIER"]

#---

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
#---

    def chat(self):
          print("you just chatted (wip)")
          self.friendship = min([self.friendship + relationship_adder, 255])
          print(f"Your friendshipp is now {self.friendship}")
          self.check_relationship()
#---
    
    def flirt(self):
          print("you just flirt (wip)")
          self.friendship = min([self.friendship + relationship_adder, 255])
          print(f"Your friendshipp is now {self.friendship}")
          self.check_relationship()
#---

    def check_relationship(self):
          if self.friendship > 100 and self.relationship == relationship_states["SOLDIER"]:
                print("now you are friends")
                self.relationship = relationship_states["FRIEND"]
          if self.friendship > 220 and self.relationship == relationship_states["FRIEND"]:
                print("now you are Best Friends!")
                self.check_relationship = relationship_states["BEST_FRIENDS"]
          if self.love > 100 and self.relationship == relationship_states["SOLDIER"]:
                print("now this is your love!")
                self.check_relationship = relationship_states["LOVE"]
          if self.friendship > 220 and self.relationship == relationship_states["LOVE"]:
                print("now this is a true love!")
                self.check_relationship = relationship_states["TRUE_LOVE"]
#---
    


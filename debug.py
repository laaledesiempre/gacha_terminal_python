from classes.constants import levels
from classes.card import Card
import random

cards = []
while True:
    print("""Debug menu, try some things!
      
      1) Create cards
      2) Erase cards
      3) See cards
      s) exit

      
      """)

    option = input("option selected: ")

    if option == "1":
        while True:
            try:
                amount = int(input("Insert amount of cards: "))
                break
            except:
                print("No valid number")

        for _ in range(amount):
            cards.append(Card(levels[random.choice(list(levels.keys()))]))
            
            
        print(f"Added {amount} of Cards")
    
    elif option == "2":
        cards = []
        print("Cards erased")
    elif option == "3":
        for i, x in enumerate(cards):
            print(f"{i} :{x.name}")
        number = input("Choose a number or write anything to exit: ")
        try:
            card_selected = cards[int(number)]
            while True:
                print(f"""
{card_selected.name}
            Options:
                1) chat.
                2) flirt.
                3) show.
                else) exit 
                """)
                selected = input("select: ")
                if selected == "1":
                    card_selected.chat()
                elif selected == "2":
                    card_selected.flirt()
                elif selected == "3":
                    print(card_selected.show())    
                else:
                    break
        except:
            pass
    elif option.lower() == "s":
        break
    else:
        print("This option is not valid or implemented")

    

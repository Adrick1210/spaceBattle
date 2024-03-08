import random

## SHIPS 
class Ship:
    
    def __init__(self, name):
        self.name = name
        self.hull = random.randint(15,25)
        self.shield = random.randint(1,5)
        self.firepower = random.randint(5,10)
        self.accuracy = random.randint(1,7)
        

    def attack(self, other):
        if(random.randint(1, 7) <= self.accuracy):
            damage = self.firepower - other.shield
            other.hull -= damage
            print(f"{self.name} blasted {other.name} for {damage} damage, they have {other.hull} left")
        else:
            print(f"{self.name} fails to attack {other.name}")
        
## FUNCTIONS  

def win_conditions(self, other):
    if(self.hull < 1):
        print("Your ship is destroyed")
        return True
    if(other.hull < 1):
        print(f"{ship.name} has destroyed the {other.name}!")
        return True
    return False     

## GAME SETUP
ship_name = input("What UNSC cruiser are you flying? ")
ship = Ship(ship_name)
banshee = Ship("banshee")

## GAME LOOP(S)
while(True):
    choice = input("The Covenant are attacking! Get into action soldier! [f]ire, [s]hields, [q]uit? ")
    
    if(choice == "f"):
        ship.attack(banshee)
        banshee.attack(ship)

    if(choice == "s"):
        ship.shield += 2
        banshee.attack(ship)
        ship.shield -= 2
    
    if(choice == "q"):
        print("Game Over")
        break
    
    if(win_conditions(ship, banshee)):
        break
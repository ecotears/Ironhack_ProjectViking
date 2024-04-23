import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        # your code here
    
    def attack(self):
        return self.strength
        # your code here

    def receiveDamage(self, damage):
        self.health -= damage
        # your code here
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        # your code here

    def battleCry(self):
        return "Odin Owns You All!"
        # your code here

    def receiveDamage(self, damage):

        self.health -= damage

        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
        # your code here


# Saxon

class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)
        # your code here

    def receiveDamage(self, damage):
        super().receiveDamage(damage)

        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'
        # your code here

# # Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        # your code here

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        # your code here
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        # your code here

    def vikingAttack(self):
        print(self.saxonArmy)
        saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        viking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]

        result = saxon.receiveDamage(viking.attack())

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
        # your code here
    
    def saxonAttack(self):
        
        saxon = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]
        viking = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]

        result = viking.receiveDamage(saxon.attack())

        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        # your code here

        return result

    def showStatus(self):
        
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
        # your code here
    pass

jugadoresVikingos = {
    'Oscar':{
        'health':10,
        'strength':8,
    },
    'Aroa':{
        'health':10,
        'strength':8,
    },
    'Patri':{
        'health':10,
        'strength':8,
    },
    'Raúl':{
        'health':10,
        'strength':8,
    }
}



guerra = War()

for name in jugadoresVikingos:
    guerra.addViking(Viking(name,jugadoresVikingos[name]['health'],jugadoresVikingos[name]['strength']))

for i in range(0,4):
    guerra.addSaxon(Saxon(5,5))


result = ''
while result != 'Vikings have won the war of the century!':

    ataqueVikingo = guerra.vikingAttack()
    print(ataqueVikingo)
    result = guerra.showStatus()
    if result != 'Vikings have won the war of the century!':
        ataqueSaxon = guerra.saxonAttack()
        print(ataqueSaxon)

    result = guerra.showStatus()
    print(result)



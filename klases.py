class gainedFruit:
    def __init__(self, species, amount, fruit):
        self.species = species
        self.amount = amount
        if fruit == True:
            self.fruit = "fruit"
            return
        self.fruit = "vegetable"
        if species == "":
            print = ""
        if amount == "":
            print = ""

    def info(self):
        print(self.species, self.amount, self.fruit)


    def add(self, amount):
        self.amout = self.amount + amount
    
    def val(self):
        return str(self.species) + " " + str(self.amount) + "kg " + str(self.fruit)
    
class Ievarijums(gainedFruit):
    def __init__(self, species, amount):
        super().__init__(species, amount, "ievārījums")
    
    def uztaisitIevarijumu(self, amount):
        if amount>self.amount/2:
            print("Nav pietiekami lai uztaisītu ievārijumu.")
            return
        self.amount = self.amount - amount*2
        print("Uztaisīja ", amount, " kg ievārijumu")
        return Ievarijums(self.species+" jam", amount)


class Carro:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("O carro: " + self.model + " está sendo pilotado")

    def stop(self):
        print("O carro: " + self.model + " está parado")

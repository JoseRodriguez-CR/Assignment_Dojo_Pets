from Pet import Pet

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__( self, first_name, last_name, pet, treats, pet_food ):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk( self ):
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed( self ):
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe( self ):
        self.pet.noise()
        return self

    #method to test the code
    def display_ninja_info( self ):
        petInfo = self.pet.display_pet_info()
        print(f"Ninja name: {self.first_name} {self.last_name}, Pet: {petInfo}, Treats: {self.treats}, Pet food: {self.pet_food}")
        return self

    

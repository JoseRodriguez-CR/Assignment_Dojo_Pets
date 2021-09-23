

class Pet:

    def __init__( self,  name , type , tricks  ):
        self.name = name
        self.type  = type 
        self.tricks = tricks
        self.energy = 100
        self.healthy = 100

    # sleep() - increases the pets energy by 25
    def sleep( self ):
        self.energy = self.energy + 25
        print(f"{self.name} has sleep and its energy increase {self.energy} units.")
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat( self ):
        self.energy = self.energy + 5
        self.healthy = self.healthy + 10
        print(f"{self.name} has eat, so its energy increase {self.energy} units and its healthy increase {self.healthy} units.")
        return self

    # play() - increases the pet's health by 5
    def play( self ):
        self.healthy = self.healthy + 5
        print(f"{self.name} has play, then its healthy increase {self.healthy} units.")
        #print(type(self.healthy))
        return self

    # noise() - prints out the pet's sound
    def noise( self ):
        print(f"{self.name} is barking, wauf!, wauf!, ..., wauf!, wauf!, wauf!, wauf!, wauf!, ")
        return self

    #method to test the code
    def display_pet_info( self ):
        print(f"Pet name: {self.name}, Type: {self.type}, Tricks: {self.tricks}, Energy: {self.energy}, Healthy: {self.healthy}")
        return self




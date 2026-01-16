# Pet class

class Pet:
    def __init__(self):
        '''This initializes the pet with its attributes.'''

        self.name = None            # stores the pet's name as a string
        self.bored = False          # stores if the pet is bored 
        self.species = None
        self.tired = True

    def set_name(self, name):
        '''This method sets the name attribute'''

        self.name = name
    
    def set_species(self, species):
        '''This method sets the name attribute'''

        self.species = species

    def introduce(self):
        '''This method introduces the pet with its name.'''

        print(f"👋 Hi, I am {self.name} and I am a {self.species}!")

    def play(self):
        '''If the pet is bored, then the pet will play. 
           If the pet just played, then it is not bored and doesn't want to play.
        '''

        if self.bored == True:          
            print("Wooooo, running!")
            self.bored = False
            self.tired = True        
        else:
            print("I don't want to play right now")
            self.bored = False 
    
    def nap(self):
        if self.tired == True:          
            print("Zzz...")
            self.tired = False 
            self.bored = True         
        else:
            print("I don't want to take a nap right now")

            


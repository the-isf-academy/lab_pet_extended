################################
# interface for the Pet object
# ----------
# edit the code below to implement the logical flow of the game
################################

from pet import Pet                             # imports the Pet class from pet.py
from helpers import menu                        # import menu 

game_play = True

# initialize pet
pet1 = Pet()

# set name
print("What would you like to name your pet?")
name = input(" > ")
pet1.set_name(name)

# set species
print("What is the species of your pet?")
species = input(" > ")
pet1.set_species(species)

menu_options = ["Introduce", "Play", "Nap", "Quit"]

while game_play == True:

    chosen_option = menu("Menu",menu_options)

    if chosen_option == 'Introduce':
        pet1.introduce()

    elif chosen_option == 'Play':
        pet1.play()
    
    elif chosen_option == 'Nap':
        pet1.nap()

    elif chosen_option == 'Quit':
        game_play = False

        
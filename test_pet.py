# a simple file to test your Pet

from pet import Pet  


pet1 = Pet()                # create an instance of a Pet
pet1.set_name("Peanut")     # call `set_name()` method
print(pet1.name)            # print the `name` attribute 

pet1.set_species("Dog")

# 💻  call `introduce()`` method
pet1.introduce()

# 💻  call `play()` method
pet1.play()

# 💻  print the `bored` attribute
print(pet1.bored)


print(pet1.species)

pet1.tired = True
pet1.nap()
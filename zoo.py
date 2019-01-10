# Create a tuple named zoo
zoo = ("Lizard", "Fox", "Mammoth")

# Find an animal's index
print(zoo.index("Fox"))

# Determine if an animal is in your tuple by using value in tuple
lizard_check = "Lizard" in zoo
print(lizard_check)

# Create a variable for each animal in the tuple
(lizard, fox, mammoth) = zoo

# Convert to a list
zoo_list = list(zoo)

# Extend list with more animals
zoo_list.extend(["Giraffe", "Zebra", "Quokka"])

# Convert back to a tuple
zoo = tuple(zoo_list)

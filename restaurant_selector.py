print("Restaurant Selector")

vegetarian = input("Is anyone in your party a vegetarian?(yes/no)").lower()
vegan = input("Is anyone in your party a vegan?(yes/no)").lower()
gluten_free = input("is anyone in your party gluten-free?(yes/no)").lower()

if vegetarian=="no" and vegan=="no" and gluten_free=="no":
    print("Here are your restaurant choices: \n Joe's Gourmet Burgers \nMain Street Pizza Company \nCorner Cafe \nMama's Fine Italian Restaurant \nThe Chef's Kitchen")
elif vegan=="yes" and vegetarian=="yes" and gluten_free=="yes":
    print("Here are your restuaurant choices: \nCorner Cafe \nThe Chef's Kitchen")
elif vegetarian=="yes" and vegan=="no" and gluten_free=="no":
    print("Here are your restuarant choices: \nMain Stree Pizza Company \nCorner Cafe \nMama's Fine Italian \nThe Chef's Kitchen")
elif vegetarian=="yes" and vegan=="yes" and gluten_free=="no":
    print("Here are your restaurant choices: \nCorner Cafe \nThe Chef's Kitchen")
elif vegetarian=="yes" and vegan=="no" and gluten_free=="yes":
    print("Here are your restaurant choices: \nMain Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")
elif vegetarian=="no" and vegan=="yes" and gluten_free=="yes":
    print("Here are your restaurant choices: \nCorner's Cafe \nThe Chef's Kitchen")
elif vegetarian=="no" and vegan=="no" and gluten_free=="yes":
    print("Here are your restaurant choices: \nMain Street Pizza Company \nCorner Cafe \nThe Chef's Kitchen")
elif vegetarian=="no" and vegan=="yes" and gluten_free=="no":
    print("Here are your restaurant choices: \nCorner Cafe \nThe Chef's Kitchen")

# 1. TASK: print "Hello World"
print( 'Hello World' )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( "Hello ", name )	# with a comma
print( "Hello " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( "Hello ", name )	# with a comma
print( "Hello " + str(name) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {} and {}.".format(fave_food1, fave_food2) ) # with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." ) # with an f string

first_name = "Eli"
print("Hello", first_name)

print("Hello " + first_name)
favorite_number = 21
print("Hello", favorite_number)
print("Hello " + str(favorite_number))

fav_food_one = "Tacos"
fav_food_two = "Burritos"

print("I love to eat {} and {}.".format(fav_food_one, fav_food_two))
print( f"I love to eat {fav_food_one} and {fav_food_two}." )

statement = "I love to eat {} and {}.".format(fav_food_one, fav_food_two)

print(first_name.lower())
print(fave_food1.upper())
print(fave_food2.title())
print(statement.split())

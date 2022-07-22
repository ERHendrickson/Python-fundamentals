from classes.deck import Deck
import random

bicycle = Deck()

# bicycle.show_cards()

# print(random.choice(bicycle.cards))

# card1 = random.choice(bicycle.cards)
# card2 = random.choice(bicycle.cards)
# card1.card_info()
# card2.card_info()

# player1 = []
# player2 = []

# player1.append(card1)
# player1.append(card2)

# player1[0].card_info()
# player1[1].card_info()



# player1_hand = player1[0].point_val + player1[1].point_val
# print(player1_hand)


"""##RULES OF 21, more or less###
give 2users two random cards
sum those cards together
ask user1 if they want another random card
  loop  
      if yes produce another random card
            if total is over 21 bust
      if no, hold "tap"

ask user2 if they want another random card
  loop
      if yes produce another random card
            if total is over 21 bust
      if no, hold "tap

show hands
if user1 or user2 cards == 21 that user wins
if its a tie neither win
if user1 hand > user2 hand user 1 wins
if user2 hand > user1 hand user 1 wins"""

print( "0) Get out!" )
print( "1) PLAY 21!!!!!!!" )

option = input( "select an option: " )

while option != "0":
    if option == "1":
        print("**************")
        player1 = []
        p1card1 = random.choice(bicycle.cards)
        p1card2 = random.choice(bicycle.cards)
        player1.append(p1card1)
        player1.append(p1card2)
        player1[0].card_info()
        player1[1].card_info()
        print(player1[0].point_val + player1[1].point_val)
        print("**************")
    print( "0) Get out!" )
    print( "2) Hit me!" )
    print( "10) I'm good!" )
    option = input( "You must choose:" )
    if option == "2":
        print("**************")
        p1card3 = random.choice(bicycle.cards)
        player1.append(p1card3)
        player1[0].card_info()
        player1[1].card_info()
        player1[2].card_info()
        #loop ver list
        total_points = player1[0].point_val + player1[1].point_val + player1[2].point_val
        print(total_points)
        if total_points > 21:
            print("BUSTED!!!!!!")
        elif total_points == 21:
            print("CHICKEN DINNER!")
        print("**************")

    # if option == 2:
        
        


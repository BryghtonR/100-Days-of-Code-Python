# 100 Days of Coding Day 11 Capstone project
import random
from tkinter import Y
import os

os.system('cls')
print("Welcome to Black Jack!")

# deck builder 
sA = {"Name":"Ace of Spades", "Value": 1}
s2 = {"Name":"Two of Spades", "Value": 2}
s3 = {"Name":"Three of Spades", "Value": 3}
s4 = {"Name":"Four of Spades", "Value": 4}
s5 = {"Name":"Five of Spades", "Value": 5}
s6 = {"Name":"Six of Spades", "Value": 6}
s7 = {"Name":"Seven of Spades", "Value": 7}
s8 = {"Name":"Eight of Spades", "Value": 8}
s9 = {"Name":"Nine of Spades", "Value": 9}
s10 = {"Name":"Ten of Spades", "Value": 10}
sJ = {"Name":"Jack of Spades", "Value": 10}
sQ = {"Name":"Queen of Spades", "Value": 10}
sK = {"Name":"King of Spades", "Value": 10}

hA = {"Name":"Ace of Hearts", "Value": 1}
h2 = {"Name":"Two of Hearts", "Value": 2}
h3 = {"Name":"Three of Hearts", "Value": 3}
h4 = {"Name":"Four of Hearts", "Value": 4}
h5 = {"Name":"Five of Hearts", "Value": 5}
h6 = {"Name":"Six of Hearts", "Value": 6}
h7 = {"Name":"Seven of Hearts", "Value": 7}
h8 = {"Name":"Eight of Hearts", "Value": 8}
h9 = {"Name":"Nine of Hearts", "Value": 9}
h10 = {"Name":"Ten of Hearts", "Value": 10}
hJ = {"Name":"Jack of Hearts", "Value": 10}
hQ = {"Name":"Queen of Hearts", "Value": 10}
hK = {"Name":"King of Hearts", "Value": 10}

dA = {"Name":"Ace of Diamonds", "Value": 1}
d2 = {"Name":"Two of Diamonds", "Value": 2}
d3 = {"Name":"Three of Diamonds", "Value": 3}
d4 = {"Name":"Four of Diamonds", "Value": 4}
d5 = {"Name":"Five of Diamonds", "Value": 5}
d6 = {"Name":"Six of Diamonds", "Value": 6}
d7 = {"Name":"Seven of Diamonds", "Value": 7}
d8 = {"Name":"Eight of Diamonds", "Value": 8}
d9 = {"Name":"Nine of Diamonds", "Value": 9}
d10 = {"Name":"Ten of Diamonds", "Value": 10}
dJ = {"Name":"Jack of Diamonds", "Value": 10}
dQ = {"Name":"Queen of Diamonds", "Value": 10}
dK = {"Name":"King of Diamonds", "Value": 10}

cA = {"Name":"Ace of Clubs", "Value": 1}
c2 = {"Name":"Two of Clubs", "Value": 2}
c3 = {"Name":"Three of Clubs", "Value": 3}
c4 = {"Name":"Four of Clubs", "Value": 4}
c5 = {"Name":"Five of Clubs", "Value": 5}
c6 = {"Name":"Six of Clubs", "Value": 6}
c7 = {"Name":"Seven of Clubs", "Value": 7}
c8 = {"Name":"Eight of Clubs", "Value": 8}
c9 = {"Name":"Nine of Clubs", "Value": 9}
c10 = {"Name":"Ten of Clubs", "Value": 10}
cJ = {"Name":"Jack of Clubs", "Value": 10}
cQ = {"Name":"Queen of Clubs", "Value": 10}
cK = {"Name":"King of Clubs", "Value": 10}
starting_deck = [sA, s2, s3, s4, s5, s6, s7, s8, s9, s10, sJ, sQ, sK, hA, h2, h3, h4, h5, h6, h7, h8, h9, h10, hJ, hQ, hK, dA, d2, d3, d4, d5, d6, d7, d8, d9, d10, dJ, dQ, dK, cA, c2, c3, c4, c5, c6, c7, c8, c9, c10, cJ, cQ, cK]

play_again = "y"
while play_again == "y":
    current_deck = starting_deck
    random.shuffle(current_deck)


    #Function: draw a card and remove from current_deck
    def deal_a_card(who):
        who.append(current_deck.pop())

    #Function: total value of all cards in hand
    def hand_total(who):
        total_value = 0
        for card in who:
            total_value += card["Value"]
            if card == sA or card == cA or card == dA or card == hA:
                if total_value <= 11:
                    total_value += 10
        return(total_value)


    #deal opening hands
    player_hand=[]
    dealer_hand=[]
    deal_a_card(player_hand)
    deal_a_card(dealer_hand)
    deal_a_card(player_hand)
    deal_a_card(dealer_hand)

    #Function: Show all hands
    dealer_hide = True

    def show_hands():
        os.system('cls')

        #Player
        print("Players Hand\n")
        for card in range(0,len(player_hand)):
            print(player_hand[card]["Name"])
        print(f"Player has: {hand_total(player_hand)}")

        print("\n**********************\n")

        #Dealer
        print("Dealers Hand\n")
        if dealer_hide == True:
            print(dealer_hand[0]["Name"])
            print("***Hidden Card***\n")
        elif dealer_hide == False:
            for card in range(0,len(dealer_hand)):
                print(dealer_hand[card]["Name"])
            print(f"Dealer has: {hand_total(dealer_hand)}")
        print("\n")
    show_hands()

    #Deal additional cards for player
    hit_or_stay = "h"
    while hit_or_stay == "h":
        hit_or_stay = input("Would you like to hit or stay? h/s: ")
        if hit_or_stay == "h":
            deal_a_card(player_hand)
            show_hands()
        if hand_total(player_hand) >21:
            break;
            
    #Deal additional cards for dealer
    dealer_hide = False
    while hand_total(dealer_hand)<17 and hand_total(player_hand)<=21 and hand_total(dealer_hand)<=21:
        deal_a_card(dealer_hand)
    show_hands()

    #Win/Lose/Draw
    if hand_total(player_hand)>21:
        print("Player Bust")
        print("Dealer Wins")
    elif hand_total(dealer_hand)>21:
        print("Dealer Bust")
        print("Player Wins")
    elif hand_total(player_hand) > hand_total(dealer_hand):
        print("Player Wins")
    elif hand_total(player_hand) < hand_total(dealer_hand):
        print("Dealer Wins")
    elif hand_total(player_hand) == hand_total(dealer_hand):
        print("Draw")

    #Go again?
    deal_again = input("Would you like to play another hand? y/n: ")
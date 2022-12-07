import random
import time
from replit import clear
new_game = 'y'
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_choice = [True,False,False,False] # 1 in 4 chance for the dealer to hit when sum(hand) > 17

def black_jack(hand):
    if sum(hand) == 21:
        return True

def check_soft_hand(hand,entity): #Pass by Object Reference

    if 11 in hand:
        temp_hand = [1 if i == 11 else i for i in hand] #Changes all occurences of 11 to 1, temp_hand is required so that we dont lose the reference to the Original object

        #Keep in mind this converts all aces to 1, this is not required in actual black jack, atmost one ace can be left as 11, I just wanted to demonstrate list comprehension.

        #"hand = [1 if i == 11 else i for i in hand]" doesn't work as 'hand' is merely a reference, as we have passed an Object Reference of the list to this function not the list object itself. This statement just reassigns the reference 'hand' to a newly created list object, and reference to the Original object in this function is lost, and hence doesn't modify the Original Object.

        hand.clear()
        hand.extend(temp_hand)
        print(f'{entity} converts Ace 11 to Ace 1')
        return True

    else:
        return False

while new_game == 'y':
    clear()
    player_bust = False
    hit = 'y'
    player_hand = [random.choice(cards),random.choice(cards)]
    dealer_hand = [random.choice(cards),random.choice(cards)]
    print(f"One card of Dealer's Hand: {dealer_hand[0]}")
    print(f"Your Hand: {player_hand}, Total = {sum(player_hand)}")

    if black_jack(player_hand) and black_jack(dealer_hand):
        print('Both Player and Dealer scored a natural. Its a Push!')
        break

    elif black_jack(player_hand):
        print('Player scored a natural, Player Wins!')
        break

    elif black_jack(dealer_hand):
        print('Dealer scored a natural, Dealer Wins!')
        break

    else:
        hit = input("Hit? enter 'y' for yes, press enter to stand: ")
        while hit == 'y':
           clear()
           player_hand.append(random.choice(cards)) #Hit

           if sum(player_hand) > 21 and not(check_soft_hand(player_hand,'Player')):
                print(f"Your Hand: {player_hand}, Total = {sum(player_hand)}")
                print(f"Dealer's hand: {dealer_hand}, Total = {sum(dealer_hand)}")
                print('Player Busts!\nDealer wins')
                player_bust = True
                break

           print(f"One card of Dealer's Hand: {dealer_hand[0]}")
           print(f"Your Hand: {player_hand}, Total = {sum(player_hand)}")
           hit = input("Hit? enter 'y' for yes, press enter to stand: ")

    if player_bust:
        new_game = input("Start a new game? enter 'y' or press enter to exit: ")
        continue

    clear()
    print("Dealer's turn")
    while True:
        time.sleep(1)
        print(f"Dealer's hand: {dealer_hand}, Total = {sum(dealer_hand)}")

        while sum(dealer_hand) < 17:
            print("Dealer's hand is less than 17")
            time.sleep(1)
            print('Dealer Hits!')
            dealer_hand.append(random.choice(cards))
            print(f"Your Hand: {player_hand}, Total = {sum(player_hand)}")
            print(f"Dealer's hand: {dealer_hand}, Total = {sum(dealer_hand)}")
            time.sleep(.6)

        if sum(dealer_hand) > 21 and not(check_soft_hand(dealer_hand,'Dealer')):
            print('Dealer Busts!\nPlayer wins')
            break

        elif sum(dealer_hand) > sum(player_hand):
            print('Dealer chose stand!')
            print('Dealer Wins!')
            break

        elif sum(player_hand) == 21 and sum(dealer_hand) == 21: #Dealer has to stand
            print('Dealer chose stand')
            print('Its a Draw!')
            break

        elif sum(player_hand) > sum(dealer_hand) and random.choice(dealer_choice): #Dealer chooses to hit or stand
            print('Dealer Hits!')
            dealer_hand.append(random.choice(cards))
            continue

        else:
            print('Dealer chose to stand!')
            if sum(player_hand) == sum(dealer_hand):
                print('Its a Draw!')
                break
            else:
                print('Player Wins!')
                break

    new_game = input("Start a new game? enter 'y' or press enter to exit: ")

# Dictionary Demo
from replit import clear

more_people = 'yes'
bidder_dict = {}
highest_bid = 0

while more_people == 'yes':
    clear()
    print(f'Current highest bid: ${highest_bid}')
    name = input('What is your name? : ')
    bid = int(input('Bid? : $'))

    if bid <= highest_bid:
        while True: #Prompting the user to enter a higher bid until the user does
            clear()
            print(f'Current highest bid: ${highest_bid}')
            bid = int(input('Enter a higher bid: ')) #This kinda makes it so the last guy to bid wins, making dictionaries or lists useless lol
            if bid > highest_bid:
                highest_bid = bid
                break
    else:
        highest_bid = bid

    bidder_dict[bid] = name #Used bid as a key to make it easier to retrieve the name of the highest bidder, as there can't be same bids in an auction
    more_people = input('Anymore people?, if so type yes, if not press enter: ')

highest_bidder = bidder_dict[highest_bid]
print(f'{highest_bidder} has won the auction with a bid of ${highest_bid}')

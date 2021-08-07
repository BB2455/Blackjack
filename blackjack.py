# Randomly pick cards
# Ask if you want to stop or grab a card

import random
from time import sleep

DELAY_MESSAGE_TIME = 1.2
SUITS = {'Diamonds', 'Hearts', 'Clubs', 'Spades'}
CARDS_VALUE = {
    'Ace' : 11,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'Jack' : 10,
    'Queen' : 10,
    'King' : 10
}

cards = set()


def setup_cards() -> None:
    for suit in SUITS:
        for name in CARDS_VALUE:
            card = name + " " + suit
            cards.add(card)


def pick_card() ->str:
    card = random.choice(tuple(cards))
    cards.remove(card)
    return card


def get_cards(num:int) -> list:
    pickedCards = []
    for _ in range(num):
        card = pick_card()
        pickedCards.append(card)
    return pickedCards


def get_total(deck:list) -> int:
    total = 0
    for card in deck:
        for name in CARDS_VALUE:
            if card.find(name) == 0:
                total += CARDS_VALUE[name]
    return total


def init() -> None:
    #Initializes the program
    setup_cards()
    currentCards = get_cards(2)
    total = get_total(currentCards)
    dealerCards = get_cards(2)
    print('The Dealer currently has one unknown card and the ' + str(dealerCards[1]))
    sleep(DELAY_MESSAGE_TIME)
    print('Current Deck: ' + ', '.join([x for x in currentCards]) + '\nCurrent Total: ' + str(total))
    sleep(DELAY_MESSAGE_TIME)
    ask_hit(currentCards, dealerCards)


def end_game(deck:list, dealerDeck:list) -> None:
    total = get_total(deck)
    dealerTotal = get_total(dealerDeck)
    if dealerTotal > total:
        print("You Lost! Your total: " + str(total) + " Dealer Total: " + str(dealerTotal))
    elif total > 21:
        print("You Lost! Your total: " + str(total) + " Dealer Total: " + str(dealerTotal))
    elif total == dealerTotal:
        print("You Tied!  Your total: " + str(total) + " Dealer Total: " + str(dealerTotal))
    elif total == 21:
        print("Blackjack! Your total: " + str(total) + " Dealer Total: " + str(dealerTotal))
    else:
        print("You Won! Your total: " + str(total) + " Dealer Total: " + str(dealerTotal))


def ask_hit(deck:list, dealerDeck:list) -> None:
    key = input('\nWould you like to Hit(Y) or Stand(N)?\n')
    #print('\n')
    if key.lower() == 'y':
        card = pick_card()
        print("You got " + card)
        sleep(DELAY_MESSAGE_TIME)
        deck.append(card)
        print('Current Deck: ' + ', '.join(deck) + '\nCurrent Total: ' + str(get_total(deck)) + '\n')
        sleep(DELAY_MESSAGE_TIME)
        if get_total(deck) > 21:
            end_game(deck, dealerDeck)
        elif get_total(deck) == 21:
            end_game(deck, dealerDeck)
        else:
            print('The Dealer currently has one unknown card and the ' + str(dealerDeck[1]))
            sleep(DELAY_MESSAGE_TIME)
            ask_hit(deck, dealerDeck)
    elif key.lower() == 'n':
        end_game(deck, dealerDeck)
    else:
        print("Invalid Command")
        ask_hit(deck, dealerDeck)


if __name__ == "__main__":
    print("\nWelcome to Blackjack!")
    init()
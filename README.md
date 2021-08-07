# Blackjack CLI

Simple blackjack game using python that is run in the terminal.

## How it works

On being called the function init will run setting up everything necessary for the game:

- Setting up cards by looping through the types of suits (Diamonds, Hearts, etc..), then looping through each value (10, J, Q, etc..) and placing each value into a set called cards.
- Getting first two cards for the player and dealer from the get_cards function which will take a parameter of how many to take from the cards set.
- Print statements which will show one card of the dealer and current score of the player with a delay which can be edited at the top of the file called "DELAY_MESSAGE_TIME".
- ask_hit function will pass player and dealer cards and will recursively run until the player total hits 21 or above or stands with current cards which will run the end_game function declaring who won.

## Installation

Download the repository and place it in desired file location.

## Usage

Call the blackjack.py file in the terminal with python.

```bash
python blackjack.py
```

When run it show you your current total and cards along with one dealer card:

```bash
Welcome to Blackjack!
The Dealer currently has one unknown card and the 8 Clubs
Current Deck: Ace Clubs, Jack Diamonds
Current Total: 21
```

It will then ask you to hit or stand, type "Y" to hit or "N" to stand (Not case sensitive). Typing anything else will get a invalid command prompt and ask you again to hit or stand.

```bash
Would you like to Hit(Y) or Stand(N)?
```

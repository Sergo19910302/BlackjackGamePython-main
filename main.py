import random

import art
# Added some style to the game using ASCII art
from art import logo

#Returns a random card from the deck.
def deal_card():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2: # Check if the cards sum up to 21 and return 0 if it's a BlackJack
        return 0
    # Check if there's an ace and the score is over 21, replace the first ace in the list by a one.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Function to compare scores, and return a string with the logo
def compare(user_score, computer_score):

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"

    if user_score == computer_score:
        return  art.draw
    elif computer_score == 0:
        return art.lose_apponent_has_blackjack
    elif user_score == 0:
        return art.blackjack
    elif user_score > 21:
        return art.lose_went_over_you_lose
    elif computer_score > 21:
        return art.opponent_went_over_you_win
    elif user_score > computer_score:
        return art.win
    else:
        return art.lose

#Function to play a game of blackjack
def play_game():
   #print logo
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#loop for play game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

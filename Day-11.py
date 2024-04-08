from art11 import logo
import random


print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, oppenent has a blackjack😱"
    elif user_score == 0:
        return "Win with a blackjack😎"
    elif user_score > 21:
        return "You went over 21. You lost🥺"
    elif comp_score > 21:
        return "You won!!! The computer went over 21😁"
    elif user_score > comp_score:
        return "You won!!!😎"
    else:
        return "You lost🥺"
    
def play_game():
    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2): 
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not is_game_over:
        user_score =  calculate_score(user_cards)
        comp_score =  calculate_score(comp_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")


        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card or type 'n' to pass: \n")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)


    print(f"        Your final hand: {user_cards}, final score: {user_score}")
    print(f"        Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))



while input("Do you want to play a game of BlackJack again? Type 'y' for yes or 'n' for no") == 'y':
    play_game()
import random
import art

print(art.ascii_art)

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_card(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, Opponent Has BlackJack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You lose"

def play_game():
    user_card = []
    computer_card = []
    game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())  # Fix: Deal different cards to computer

    while not game_over:    
        user_score = calculate_card(user_card)
        computer_score = calculate_card(computer_card)
        
        print(f'Your Cards: {user_card}, current score: {user_score}')
        print(f'Computer first Card: {computer_card[0]}')
            
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_input_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_input_deal == 'y':
                user_card.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_card(computer_card)
    
    print(f"Your final hand is: {user_card}, final score: {user_score}")
    print(f"Computer's final hand is: {computer_card}, final score: {computer_score}")
    
    # Fix: Pass correct variables to compare function
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ") == 'y':
    print("\n" * 5)
    play_game()

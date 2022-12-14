import random
from os import system, name
from art import logo

################################
def clear():
    """Function to clear console"""
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')
################################

def get_card():
    """Deals a card"""
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    card = random.choice(cards)
    return card

def total_score(cards):
    """Sums up the total value of all cards at hand"""
    total = 0

    for i in range(len(cards)):
        if cards[i] == 'A':
            total += 11
        elif cards[i] == 'J':
            total += 10
        elif cards[i] == 'Q': 
            total += 10
        elif cards[i] == 'K': 
            total += 10
        else:
            total += cards[i]
    
    if total == 21 and len(cards) == 2:
        return 0
    
    if total > 21:
        for _ in range(cards.count('A')):
            total -= 10

    return total

def show_hands(your_cards, house_cards, your_total, house_total):
    """Prints final hand results"""
    text = f'''
    Your final hand: {your_cards}, final score: {your_total}\n
    House's final hand: {house_cards}, final score: {house_total}\n
    '''

    if your_total == 0 and house_total == 0:
        your_total = 21
        house_total = 21
        print(text)
        print("--> PUSH - draw. 😐")
        return True
    if your_total == 0:
        your_total = 21
        print(text)
        print ("--> You have BlackJack! You WIN. 😃")   
        return True
    if house_total == 0:
        house_total = 21
        print(text)
        print("--> House has BlackJack! You LOSE. 😥")
        return True

def check_for_blackjack(your_cards, house_cards, your_total, house_total):
    """Checks if any players have blackjack"""
    return True if show_hands(your_cards, house_cards, your_total, house_total) else False

def compare(your_total, house_total):
    """Compare scores and determines winner in all scenarios."""
    if your_total == house_total:
        print("---> PUSH - draw. 😐\n")
    elif house_total == 0:
        print("---> You LOSE. 😥\n")
    elif your_total == 0:
        print ("---> You WIN! 😃\n")
    elif house_total > 21:
        print ("---> You WIN! 😃\n")
    elif your_total > 21:
        print ("---> You LOSE! 😥\n")
    elif your_total > house_total:
        print("---> You WIN! 😃\n")
    else:
        print("---> You LOSE! 😥\n")

def end_game(your_cards, house_cards, your_total, house_total):
    """Prints final hand results."""
    text = f'''
    Your final hand: {your_cards}, final score: {your_total}\n
    House's final hand: {house_cards}, final score: {house_total}\n
    '''
    print(text)
    compare(your_total, house_total)


################################
def start_new_game():
    """Starts new blackjack game"""
    
    print(logo)
    your_cards = []
    house_cards = []

    #Deals first two cards for you and house
    for _ in range(2):
        your_cards.append(get_card())
        house_cards.append(get_card())

    #Condition for while loop to repeatedly for continuation
    should_continue = True
    your_total = total_score(your_cards)
    house_total = total_score(house_cards)

    if check_for_blackjack(your_cards, house_cards, your_total, house_total) == True:
        return

    while should_continue == True:
        
        text = f'''
        Your cards: {your_cards}, current score: {your_total}\n
        House's first card: [{house_cards[0]}, ?]\n
        '''
        print(text)

        if input("Type 'y' to HIT, type 'n' to STAND: ") == 'y':
            your_cards.append(get_card())
            your_total = total_score(your_cards)
            if your_total > 21:
                end_game(your_cards, house_cards, your_total, house_total)
                should_continue = False

        else: 
            while house_total < 17:
                house_cards.append(get_card())
                house_total = total_score(house_cards)
            
            should_continue = False
            end_game(your_cards, house_cards, your_total, house_total)          

################################


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    clear()
    start_new_game()
else: 
    clear()
    print("Thank you for playing BlackJack. Goodbye!")
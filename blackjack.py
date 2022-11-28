import random
from art import logo

def start_new_game():
    """Starts new blackjack game"""
    if input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
        your_cards = []
        house_cards = []
        
        def get_card():
            """Deals a card"""
            cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
            card = random.choice(cards)
            return card
    
        
        for _ in range(2):
            """Deals first two cards"""
            your_cards.append(get_card())
            house_cards.append(get_card())
            
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
        
        your_total = total_score(your_cards)
        house_total = total_score(house_cards)

        def show_hands():
            if your_total == 0:
                print(f"-> Your final hand: {your_cards}, final score: 21")
                print(f"-> Computer's final hand: {house_cards}, final score: {house_total}")
            if house_total == 0:
                print(f"-> Your final hand: {your_cards}, final score: {your_total}")
                print(f"-> Computer's final hand: {house_cards}, final score: 21")


        def check_for_blackjack():
            if your_total == 0 and house_total == 0:
                show_hands()
                print("---> PUSH - draw. 🙃")
                start_new_game()
            elif house_total == 0:
                show_hands()
                print("---> House has BlackJack! You LOSE. 😥")
                start_new_game()
            elif your_total == 0:
                show_hands()
                print ("---> You have BlackJack! You WIN. 😃")    
                start_new_game()         


        def compare():
            """Compare scores and determines winner in all scenarios."""
            if your_total == house_total:
                print("---> PUSH - draw. 🙃\n")
            elif house_total == 0:
                print("---> House WINS. You LOSE. 😥\n")
            elif your_total == 0:
                print ("---> You WIN. 😃\n")
            elif house_total > 21:
                print ("---> You WIN. 😃\n")
            elif your_total > 21:
                print ("---> You LOSE. 😃\n")
            elif your_total > house_total:
                print("---> You WIN. 😃\n")
            else:
                print("---> You LOSE. 😥\n")


        def end_game():
            """Prints final hand results and requests to start a new game."""
            print(f"-> Your final hand: {your_cards}, final score: {your_total}")
            print(f"-> Computer's final hand: {house_cards}, final score: {house_total}")
            compare()
            start_new_game()  
        

        #Condition for while loop to repeatedly for continuation
        should_continue = True

        print(logo)

        while should_continue == True:

            check_for_blackjack()

            print(f"-> Your cards: {your_cards}, current score: {your_total}")
            print(f"-> Computer's first card: {house_cards[0]}\n")

            if input("Type 'y' to HIT, type 'n' to STAND: ") == 'y':
                your_cards.append(get_card())
                your_total = total_score(your_cards)
                if your_total > 21:
                    end_game()
    
            else: 
                while house_total < 17:
                    house_cards.append(get_card())
                    house_total = total_score(house_cards)
                
                should_continue = False
                end_game()
                start_new_game()            

    else:
        return


start_new_game()
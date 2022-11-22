import random
from art import logo

def start_new_game():

    if input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        your_cards = []
        computer_cards = []
        
        def get_card():
            random_num = random.randint(0,12)
            card = cards[random_num]
            return card
            #House deals you your cards  
        
        your_cards.append(get_card())
        your_cards.append(get_card())
            
        #Totals your score
        def total_score(cards):
            total = 0
            for card in cards:
                total += card
            return total
        
        your_total = total_score(your_cards)
        
        #Computer's cards
        first_cpu_card = get_card()
        computer_cards.append(first_cpu_card)
        computer_total = total_score(computer_cards)
        
        #Condition for while loop to repeatedly for continuation
        should_continue = True

        print(logo)

        while should_continue == True:
            print(f"Your cards: {your_cards}, current score: {your_total}")
            print(f"Computer's first card: {first_cpu_card}")

            if input("Type 'y' to HIT, type 'n' to STAND: ") == 'y':
                your_cards.append(get_card())
                your_total = total_score(your_cards)
            else: 
                should_continue = False
                # deal_cpu_cards()
                while computer_total < 17:
                    computer_cards.append(get_card())
                    computer_total = total_score(computer_cards)
                
                print(f"Your final hand: {your_cards}, final score: {your_total}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
                
                if computer_total == 21 and your_total != 21:
                    print("You lose. 😥")
                elif your_total > 21:
                    print("You lose. 😥")
                elif your_total <= 21 and computer_total > 21:
                    print ("You win. 😃")
                elif your_total == computer_total:
                    print("Draw. 🙃")
                elif your_total > computer_total:
                    print("You win. 😃")
                else:
                    print("You lose. 😥")

                start_new_game()            

    else:
        return


start_new_game()